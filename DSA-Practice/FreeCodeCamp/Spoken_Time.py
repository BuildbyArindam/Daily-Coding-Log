"""
Problem: Spoken Time
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-06
Date: 2026-08-30

Approach:
Convert clock-hand angles into a spoken time string. The minute hand's
angle is rounded to the nearest 5-minute mark (30 degrees == 5 minutes),
and the hour hand's angle is used to derive the base hour (30 degrees == 1 hour).
Cases are branched by the minute value:
  - 0            -> "H o'clock"
  - 1-29         -> "M minutes past H" (with "quarter past H" at 15)
  - 30           -> "half past H"
  - 31-59        -> "M minutes to (H+1)" (with "quarter to (H+1)" at 45)
Hour wraps handled with modulo 12, converting 0 to 12 for 12-hour clock format.

Time Complexity: O(1) - fixed number of arithmetic operations and comparisons
Space Complexity: O(1) - no auxiliary data structures
"""


# ------------------------ Solution --------------------------------


def get_spoken_time(hour_angle, minute_angle):
    minute = round(minute_angle / 30) * 5
    hour_position = hour_angle / 30
    if minute == 0:
        hour = round(hour_position) % 12
        if hour == 0:
            hour = 12
        return f"{hour} o'clock"
    elif minute < 30:
        hour = int(hour_position) % 12
        if hour == 0:
            hour = 12
        if minute == 15:
            return f"quarter past {hour}"
        return f"{minute} minutes past {hour}"
    elif minute == 30:
        hour = round(hour_position) % 12
        if hour == 0:
            hour = 12
        return f"half past {hour}"
    else:
        next_hour = int(hour_position) + 1
        next_hour = ((next_hour - 1) % 12) + 1
        if minute == 45:
            return f"quarter to {next_hour}"
        return f"{60 - minute} minutes to {next_hour}"
