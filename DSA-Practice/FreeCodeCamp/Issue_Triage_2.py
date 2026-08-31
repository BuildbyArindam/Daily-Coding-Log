"""
Problem: Issue Triage 2
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-09
Date Solved: 2026-08-31
Difficulty: Easy-Medium
Topics: String Manipulation, Conditional Logic, List Manipulation, Rule-Based Simulation

Approach:
Classify/re-label a GitHub-style issue based on its title and current labels.
- If no labels exist, inspect the title for "error"/"bug" or "feature"/"add"
  keywords to assign initial labels.
- If labels already exist, apply transition rules: "needs triage" -> 
  "good first issue" (if title suggests simplicity), "discussing" ->
  "on the roadmap" (if title suggests it's planned), or fall back to
  "help wanted" if neither condition is met.
- Independently, append "critical" if the title mentions "security".

Time Complexity: O(n) where n = number of existing labels (due to list
                  membership checks/removals); title checks are O(1) substring lookups.
Space Complexity: O(n) for the copied labels list.
"""


# ----------------------------- Solution -----------------------------------


def triage_issue(title, labels):
    title_lower = title.lower()
    labels = labels.copy()
    if not labels:
        if "error" in title_lower or "bug" in title_lower:
            labels.extend(["bug", "needs triage"])
        elif "feature" in title_lower or "add" in title_lower:
            labels.extend(["enhancement", "discussing"])
    else:
        if "needs triage" in labels and ("simple" in title_lower or "easy" in title_lower):
            labels.remove("needs triage")
            labels.append("good first issue")
        elif "discussing" in labels and ("planned" in title_lower or "next" in title_lower):
            labels.remove("discussing")
            labels.append("on the roadmap")
        elif "needs triage" in labels or "discussing" in labels:
            if "needs triage" in labels:
                labels.remove("needs triage")
            if "discussing" in labels:
                labels.remove("discussing")
            labels.append("help wanted")
    if "security" in title_lower:
        labels.append("critical")
    return labels
