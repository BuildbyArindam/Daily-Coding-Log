#!/usr/bin/env python3
"""
Regenerate README.md from the solution files in DSA-Practice/.

Usage (from the repo root):
    python scripts/update_readme.py

Needs only the Python 3.8+ standard library.
Edit the PROFILES / PLATFORM_TOTALS sections below when your accounts or totals change.
"""
import collections, datetime as dt, os, re, sys
from urllib.parse import quote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "DSA-Practice")
OUT = os.path.join(ROOT, "README.md")
REPO = "BuildbyArindam/Daily-Coding-Log"
BASE = f"https://github.com/{REPO}/blob/main/DSA-Practice/"

# ----------------------------- EDIT ME ---------------------------------
PROFILES = {  # folder name -> (label, handle, profile URL)
    "LeetCode":      ("🟠 LeetCode", "0Arindam0_", "https://leetcode.com/u/0Arindam0_/"),
    "GeeksforGeeks": ("🟢 GeeksforGeeks", "subirouynn", "https://www.geeksforgeeks.org/user/subirouynn/"),
    "Codeforces":    ("🔵 Codeforces", "mahapatraarindam4", "https://codeforces.com/profile/mahapatraarindam4"),
    "CodeChef":      ("🟤 CodeChef", "amahapatra2004", "https://www.codechef.com/users/amahapatra2004"),
    "HackerEarth":   ("🟣 HackerEarth", "mahapatraarindam4", "https://www.hackerearth.com/@mahapatraarindam4/"),
    "Unstop":        ("🟡 Unstop", "arindmah7062", "https://unstop.com/u/arindmah7062"),
    "Code360":       ("🧡 Coding Ninjas (Code360)", "Profile", "https://www.naukri.com/code360/profile/fd676eb2-50b1-413c-aeea-3e8ea44e0a46"),
    "FreeCodeCamp":  ("⚪ freeCodeCamp", "Profile", "https://www.freecodecamp.org/fccdee8d2f5-58e1-4b09-9d09-2e7dafec471b"),
}
EXTRA_PROFILES = [("🟩 HackerRank", "mahapatraarinda1", "http://www.hackerrank.com/profile/mahapatraarinda1")]
PLATFORM_TOTALS = {  # solved on the site itself (manual; update occasionally)
    "LeetCode": 1599, "GeeksforGeeks": 1315, "Codeforces": 217, "CodeChef": 142,
    "HackerEarth": 154, "Unstop": 668, "Code360": 111, "FreeCodeCamp": 300,
}
NOTE = "_HackerRank (400 solved on the site) has no folder in this repo yet._"
GOAL_TARGET = 1500  # solutions-in-repo goal shown in the Goals list
# -----------------------------------------------------------------------

CATS = [
    ("Arrays & Prefix Sums", r"array|prefix|subarray|kadane|matrix|grid"),
    ("Strings", r"string|palindrom|substring|anagram|text"),
    ("Hashing & Maps", r"hash|map|frequency|dictionary|counting"),
    ("Two Pointers & Sliding Window", r"two.pointer|sliding|window"),
    ("Sorting & Searching", r"sort|binary search|searching|ternary"),
    ("Linked Lists", r"linked list"),
    ("Stacks, Queues & Heaps", r"stack|queue|heap|priority|deque|monotonic"),
    ("Trees", r"\btree|bst|trie|segment|fenwick|\bbit\b|hld|lca"),
    ("Graphs", r"graph|bfs|dfs|dijkstra|dsu|union|topolog|shortest|flood"),
    ("Dynamic Programming", r"\bdp\b|dynamic|memo|knapsack|tabulation"),
    ("Greedy", r"greedy"),
    ("Recursion & Backtracking", r"backtrack|recurs|permutation|subsets"),
    ("Bit Manipulation", r"bit|xor|bitmask"),
    ("Math & Number Theory", r"math|number theory|prime|gcd|modular|divisor|combinator|sieve|probability|geometry"),
    ("Implementation & Simulation", r"implement|simulat|brute|basic|i/o|conditional|constructive|loop|ad.hoc|game"),
    ("Design / OOP / SQL", r"solid|oop|design|sql|class|database|query"),
]
CODE_EXT = {".py", ".js", ".java", ".cpp", ".c", ".sql", ".ts", ".go", ".rs", ".kt", ".cs"}


def rating_of(text):
    m = re.search(r"(\d{3,4})", text)
    return int(m.group(1)) if m else None


def normalise(plat, diff, head):
    d = diff.lower()
    num = rating_of(d) if not re.search("[a-z]", d) else None
    if num is None and plat == "Codeforces":
        m = re.search(r"\*(\d{3,4})", head)
        num = int(m.group(1)) if m else rating_of(d)
    if num is not None:
        if plat == "CodeChef":
            return "Easy" if num < 1200 else "Medium" if num < 1800 else "Hard"
        return "Easy" if num <= 1200 else "Medium" if num <= 1900 else "Hard"
    if "medium" in d and "hard" in d: return "Hard"
    if "easy" in d and "medium" in d: return "Medium"
    if any(k in d for k in ("cakewalk", "easy", "beginner")): return "Easy"
    if "medium" in d: return "Medium"
    if "hard" in d: return "Hard"
    return "Unrated"


def read_rows():
    rows = []
    for plat in sorted(os.listdir(SRC)):
        pdir = os.path.join(SRC, plat)
        if not os.path.isdir(pdir): continue
        for f in sorted(os.listdir(pdir)):
            if os.path.splitext(f)[1].lower() not in CODE_EXT: continue
            head = open(os.path.join(pdir, f), encoding="utf-8", errors="ignore").read(3500)
            d = re.search(r"(?:Difficulty|Rating|Level)\s*[:=]\s*([^\n|]+)", head, re.I)
            diff = d.group(1).strip() if d else ""
            if not diff:
                m = re.search(r"\*(\d{3,4})", head)
                diff = "*" + m.group(1) if m else ""
            t = re.search(r"(?:Topics?|Tags?)\s*[:=]\s*([^\n]+)", head, re.I)
            topics = re.sub(r"\|\s*Rating.*", "", t.group(1).strip()) if t else ""
            dm = re.search(r"Date(?: Solved)?\s*[:=]\s*(\d{4}-\d{2}-\d{2})", head)
            low = head.lower()
            cats = [n for n, k in CATS if re.search(k, topics.lower())]
            if not cats:
                cats = [n for n, k in CATS if re.search(k, low)][:2] or ["Implementation & Simulation"]
            cf = None
            if plat == "Codeforces":
                cf = rating_of(diff) or (int(m.group(1)) if (m := re.search(r"\*(\d{3,4})", head)) else None)
            rows.append(dict(plat=plat, file=f, date=dm.group(1) if dm else "", cats=cats,
                             nd=normalise(plat, diff, head), cf=cf))
    return rows


def bar(v, t, w=20):
    f = round(w * v / t) if t else 0
    return "█" * f + "░" * (w - f)


def build(rows):
    N = len(rows)
    plats = sorted({r["plat"] for r in rows} | set(PROFILES), key=lambda p: -sum(r["plat"] == p for r in rows))
    cnt = collections.Counter(r["plat"] for r in rows)
    dif = collections.Counter(r["nd"] for r in rows)
    topics = collections.Counter(c for r in rows for c in r["cats"])
    langs = collections.Counter(os.path.splitext(r["file"])[1].lower() for r in rows)
    dates = sorted({dt.date.fromisoformat(r["date"]) for r in rows if r["date"]})
    best = cur = 1 if dates else 0
    for a, b in zip(dates, dates[1:]):
        cur = cur + 1 if (b - a).days == 1 else 1
        best = max(best, cur)
    streak, today, ds = 0, dt.date.today(), set(dates)
    day = today if today in ds else today - dt.timedelta(days=1)
    while day in ds:
        streak += 1; day -= dt.timedelta(days=1)
    prof = lambda p: PROFILES.get(p, (p, "", "#"))
    L = []; w = L.append
    typed = f"{N:,}".replace(",", "%2C")
    w(f'''<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:8957e5&height=220&section=header&text=Daily%20Coding%20Log&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=One%20problem%20at%20a%20time.%20Every%20single%20day.&descAlignY=58&descSize=18" width="100%"/>

<a href="https://github.com/BuildbyArindam"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=58A6FF&center=true&vCenter=true&width=700&lines={typed}+solutions+committed+and+counting;{len(plats)}+platforms+%7C+Python+%7C+JavaScript+%7C+Java+%7C+SQL;Consistency+over+intensity+%F0%9F%9A%80"/></a>

![Solutions](https://img.shields.io/badge/Solutions%20Uploaded-{N}-1f6feb?style=for-the-badge&logo=github&logoColor=white)
![Platforms](https://img.shields.io/badge/Platforms-{len(plats)}-8957e5?style=for-the-badge)
![Streak](https://img.shields.io/badge/Current%20Streak-{streak}%20days-f78166?style=for-the-badge)
![Active](https://img.shields.io/badge/Active%20Days-{len(dates)}-3fb950?style=for-the-badge)
![Hard](https://img.shields.io/badge/Hard%20Solved-{dif["Hard"]}-f85149?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-{langs[".py"]}-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-{langs[".js"]}-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Java](https://img.shields.io/badge/Java-{langs[".java"]}-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-{langs[".sql"]}-4479A1?style=flat-square&logo=mysql&logoColor=white)
![C++](https://img.shields.io/badge/C++-{langs[".cpp"]}-00599C?style=flat-square&logo=cplusplus&logoColor=white)

</div>

---

## ⚡ At a Glance

| 🧮 Solutions in repo | 🟢 Easy | 🟡 Medium | 🔴 Hard | 📅 Active days | 🔥 Longest streak |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **{N:,}** | **{dif["Easy"]}** | **{dif["Medium"]}** | **{dif["Hard"]}** | **{len(dates)}** | **{best} days** |

> 📆 Logging window: **{dates[0]:%d %b %Y} → {dates[-1]:%d %b %Y}** &nbsp;•&nbsp; Every file has a header with problem link, date, difficulty, topics, approach and complexity.

---

## 🔗 Coding Profiles

<div align="center">

| Platform | Handle | Link |
|:--|:--|:--:|''' if dates else "")
    for p in PROFILES:
        lab, h, url = PROFILES[p]; w(f"| {lab} | `{h}` | [Visit]({url}) |")
    for lab, h, url in EXTRA_PROFILES: w(f"| {lab} | `{h}` | [Visit]({url}) |")
    w('''
<img src="https://leetcode-stats-six.vercel.app/?username=0Arindam0_&theme=dark" height="170"/>
<img src="https://codeforces-readme-stats.vercel.app/api/card?username=mahapatraarindam4&theme=dark" height="170"/>

</div>

---

## 📂 Repository Structure

```text
Daily-Coding-Log/
└── DSA-Practice/''')
    for i, p in enumerate(plats):
        w(f'    {"└──" if i == len(plats) - 1 else "├──"} {p + "/":<16} # {cnt[p]} solutions')
    w('''```

---

## 📊 Progress by Platform

> **In repo** = solution files uploaded here (counted automatically). **Platform total** = problems solved on the site itself (manual figures).

| Platform | In repo | Share | Platform total | 🟢 Easy | 🟡 Medium | 🔴 Hard | ⚪ Unrated |
|:--|--:|:--|--:|--:|--:|--:|--:|''')
    for p in plats:
        c = collections.Counter(r["nd"] for r in rows if r["plat"] == p)
        tot = f"{PLATFORM_TOTALS[p]:,}" if p in PLATFORM_TOTALS else "–"
        w(f"| [{p}]({prof(p)[2]}) | **{cnt[p]}** | `{bar(cnt[p], N, 12)}` {cnt[p] / N * 100:.0f}% | {tot} | {c['Easy']} | {c['Medium']} | {c['Hard']} | {c['Unrated']} |")
    w(f"| **Total** | **{N:,}** | | | **{dif['Easy']}** | **{dif['Medium']}** | **{dif['Hard']}** | **{dif['Unrated']}** |")
    w(f"\n{NOTE}\n\n### 🎯 Difficulty Split\n\n```mermaid\npie showData title Difficulty distribution (all platforms)")
    for k in ("Easy", "Medium", "Hard", "Unrated"): w(f'    "{k}" : {dif[k]}')
    w('''```

> **How difficulty is normalised:** Easy / Cakewalk / Beginner → Easy · Easy-Medium → Medium · Medium-Hard → Hard · Codeforces ≤1200 Easy, 1300–1900 Medium, 2000+ Hard · CodeChef rating <1200 Easy, 1200–1799 Medium, 1800+ Hard · files with no difficulty label → Unrated.

---

## 🧩 Progress by Topic

> A solution can carry several topics, so the counts add up to more than the total.

| Topic | Solutions | Distribution |
|:--|--:|:--|''')
    mx = max(topics.values())
    for k, v in topics.most_common(): w(f"| {k} | **{v}** | `{bar(v, mx, 24)}` |")
    cf = [r for r in rows if r["plat"] == "Codeforces" and r["cf"]]
    if cf:
        bands = [("≤ 1200", 0, 1200), ("1300 – 1600", 1201, 1600), ("1700 – 1900", 1601, 1900), ("2000 – 2300", 1901, 2300), ("2400+", 2301, 10**5)]
        cb = {n: sum(lo <= r["cf"] <= hi for r in cf) for n, lo, hi in bands}
        w("\n---\n\n## 🏆 Codeforces Rating Ladder\n\n| Rating band | Solved | |\n|:--|--:|:--|")
        for n, _, _ in bands: w(f"| {n} | **{cb[n]}** | `{bar(cb[n], max(cb.values()), 20)}` |")
        w("\n### 💎 Hall of Fame (hardest solved)\n\n| Rating | Problem | Solution |\n|:--:|:--|:--:|")
        for r in sorted(cf, key=lambda r: -r["cf"])[:8]:
            nm = re.sub(r"^\d+[A-Z]?\d?[-_]", "", os.path.splitext(r["file"])[0]).replace("_", " ").replace("-", " ")
            w(f"| ⭐ **{r['cf']}** | {nm} | [Code]({BASE}Codeforces/{quote(r['file'])}) |")
    icon = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴", "Unrated": "⚪"}
    w("\n---\n\n## 📅 Recent Activity (latest solves)\n\n| Date | Platform | Problem | Difficulty | Solution |\n|:--|:--|:--|:--:|:--:|")
    for r in sorted([r for r in rows if r["date"]], key=lambda r: (r["date"], r["file"]), reverse=True)[:15]:
        nm = os.path.splitext(r["file"])[0].replace("_", " ")
        w(f"| {r['date']} | {r['plat']} | {nm} | {icon[r['nd']]} {r['nd']} | [Code]({BASE}{r['plat']}/{quote(r['file'])}) |")
    tick = lambda ok: "x" if ok else " "
    w(f'''
---

## 🎯 Goals

- [{tick(N >= 100)}] Reach 100 solutions in this repo
- [{tick(N >= 300)}] Reach 300 solutions in this repo
- [{tick(len(plats) >= 8)}] Solve problems on 8+ platforms
- [{tick(any(r["cf"] and r["cf"] >= 2400 for r in cf))}] Solve Codeforces problems rated 2400+
- [{tick(streak >= 100)}] Keep a 100-day streak (current: **{streak}** days)
- [{tick(N >= GOAL_TARGET)}] Reach {GOAL_TARGET:,} solutions in this repo (**{N:,}** so far)

---

<div align="center">

*Consistency over intensity — one problem at a time.* 🚀

<sub>Last auto-updated: {dt.date.today():%d %b %Y} by <code>scripts/update_readme.py</code></sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8957e5,50:1f6feb,100:0d1117&height=100&section=footer" width="100%"/>

</div>
''')
    return "\n".join(L)


if __name__ == "__main__":
    rows = read_rows()
    if not rows:
        sys.exit("No solution files found in DSA-Practice/")
    open(OUT, "w", encoding="utf-8").write(build(rows))
    print(f"README.md updated: {len(rows)} solutions across {len({r['plat'] for r in rows})} platforms")
