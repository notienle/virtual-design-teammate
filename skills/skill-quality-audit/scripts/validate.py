#!/usr/bin/env python3
"""Structural validator for the virtual-design-teammates skill pack.

Usage: python3 validate.py [plugin-root]   (default: current directory)

Checks (all deterministic - judgment graders live in SKILL.md):
  1. Manifest: valid JSON, kebab-case name, version present
  2. Every skills/*/ dir has SKILL.md with parseable frontmatter
  3. Frontmatter name matches directory; description present, 50-1024 chars
  4. SKILL.md under 500 lines
  5. references/ files mentioned in a SKILL.md actually exist
  6. Skill names mentioned in routing (`backtick-quoted`) exist in skills/ or parked-skills/
  7. No duplicate skill names across active + parked

Exit code 0 = pass, 1 = failures found. Output: one line per finding, severity-tagged.
"""
import json
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
findings = []


def add(sev, loc, msg):
    findings.append(f"[{sev}] {loc}: {msg}")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


# 1. Manifest
mpath = os.path.join(ROOT, ".claude-plugin", "plugin.json")
if not os.path.exists(mpath):
    add("BLOCKER", mpath, "manifest missing")
else:
    try:
        manifest = json.load(open(mpath))
        name = manifest.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            add("BLOCKER", mpath, f"name not kebab-case: {name!r}")
        if not manifest.get("version"):
            add("MAJOR", mpath, "version missing")
    except Exception as e:  # noqa: BLE001
        add("BLOCKER", mpath, f"invalid JSON: {e}")

# Collect skill dirs
active_dir = os.path.join(ROOT, "skills")
parked_dir = os.path.join(ROOT, "parked-skills")
active = sorted(d for d in os.listdir(active_dir)) if os.path.isdir(active_dir) else []
parked = sorted(d for d in os.listdir(parked_dir)) if os.path.isdir(parked_dir) else []
parked = [d for d in parked if os.path.isdir(os.path.join(parked_dir, d))]
all_names = set(active) | set(parked)

dupes = set(active) & set(parked)
for d in dupes:
    add("BLOCKER", d, "exists in both skills/ and parked-skills/")

# 2-6 per active skill (parked skills get structural checks too, softer severity)
for base, dirs, hard in ((active_dir, active, True), (parked_dir, parked, False)):
    for s in dirs:
        p = os.path.join(base, s, "SKILL.md")
        loc = os.path.relpath(p, ROOT)
        if not os.path.exists(p):
            add("BLOCKER" if hard else "MINOR", loc, "SKILL.md missing")
            continue
        text = open(p, encoding="utf-8").read()
        lines = text.count("\n") + 1
        if lines > 500:
            add("MAJOR", loc, f"{lines} lines (limit 500) - move depth to references/")
        fm = frontmatter(text)
        if fm is None:
            add("BLOCKER" if hard else "MINOR", loc, "no YAML frontmatter")
            continue
        nm = re.search(r"^name:\s*(\S+)", fm, re.M)
        if not nm or nm.group(1) != s:
            add("BLOCKER" if hard else "MINOR", loc,
                f"frontmatter name {nm.group(1) if nm else None!r} != directory {s!r}")
        desc = re.search(r"^description:\s*>?\s*\n((?:\s{2,}.*\n?)+)", fm, re.M)
        flat = re.sub(r"\s+", " ", desc.group(1)).strip() if desc else ""
        if not flat:
            add("BLOCKER" if hard else "MINOR", loc, "description missing or empty")
        elif len(flat) < 50:
            add("MAJOR", loc, f"description too short ({len(flat)} chars) to trigger reliably")
        elif len(flat) > 1024:
            add("MAJOR", loc, f"description too long ({len(flat)} chars)")

        # referenced files exist
        for ref in re.findall(r"references/[\w\-./]+\.md", text):
            rp = os.path.join(base, s, ref)
            if not os.path.exists(rp):
                add("BLOCKER" if hard else "MINOR", loc, f"referenced file missing: {ref}")

        # routing mentions exist (backticked kebab-case tokens that look like skill names)
        if hard:
            for token in set(re.findall(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`", text)):
                if token == s or "." in token or "/" in token:
                    continue
                known_non_skills = {
                    "optimizely-brand", "skill-creator", "pcd-design-teammate",
                    "search-components", "get-tokens", "get-patterns", "search-icons",
                }
                if token in known_non_skills:
                    continue
                if token not in all_names:
                    add("MINOR", loc, f"routing mentions unknown skill `{token}`")

# Report
print(f"Scanned {len(active)} active + {len(parked)} parked skills under {os.path.abspath(ROOT)}")
if findings:
    for f in sorted(findings):
        print(f)
    blockers = sum(1 for f in findings if f.startswith("[BLOCKER"))
    majors = sum(1 for f in findings if f.startswith("[MAJOR"))
    print(f"RESULT: FAIL ({blockers} blockers, {majors} majors, {len(findings)} total)")
    sys.exit(1)
print("RESULT: PASS")
