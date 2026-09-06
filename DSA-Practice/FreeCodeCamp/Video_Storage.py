"""
Problem: Video Storage
Platform: FreeCodeCamp - Daily Coding Challenge (09-21)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-21
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Basic Math, Unit Conversion, Implementation

Approach:
    Convert both the video size and drive size to bytes using unit
    lookup dictionaries (video units: B/KB/MB/GB, drive units: GB/TB,
    all base-1000). Validate units first, then compute how many whole
    videos fit on the drive via integer floor division.

Time Complexity:  O(1) - fixed dictionary lookups and arithmetic
Space Complexity: O(1) - fixed-size lookup tables
"""


# ----------------------- Solution --------------------------------


def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    video_units = {
        "B": 1,
        "KB": 1000,
        "MB": 1000 ** 2,
        "GB": 1000 ** 3
    }
    drive_units = {
        "GB": 1000 ** 3,
        "TB": 1000 ** 4
    }
    if video_unit not in video_units:
        return "Invalid video unit"
    if drive_unit not in drive_units:
        return "Invalid drive unit"
    video_bytes = video_size * video_units[video_unit]
    drive_bytes = drive_size * drive_units[drive_unit]
    return int(drive_bytes // video_bytes)
