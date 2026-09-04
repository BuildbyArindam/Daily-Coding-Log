"""
Problem: Contrast Rating 3
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-30
Date Solved: 2026-09-04
Difficulty: Easy-Medium
Topics: Color/Luminance Calculation, Conditional Logic, WCAG Accessibility Rules, Math

Approach:
Compute the WCAG relative luminance of each RGB color using the standard
sRGB gamma-correction formula, then derive the contrast ratio between the
lighter and darker luminance. Compare against WCAG 2.1 thresholds
(different for large vs normal text) to classify as AAA / AA / Fail.

Time Complexity: O(1) — fixed 3-channel luminance calc per color
Space Complexity: O(1) — constant extra space
"""


# ------------------------ Solution -----------------------------------


def get_contrast_rating(rgb1, rgb2, is_large_text):
    def get_luminance(rgb):
        channels = []
        for channel in rgb:
            channel = channel / 255
            if channel <= 0.04045:
                channel = channel / 12.92
            else:
                channel = ((channel + 0.055) / 1.055) ** 2.4
            channels.append(channel)
        return (
            0.2126 * channels[0]
            + 0.7152 * channels[1]
            + 0.0722 * channels[2]
        )
    lum1 = get_luminance(rgb1)
    lum2 = get_luminance(rgb2)
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    contrast_ratio = (lighter + 0.05) / (darker + 0.05)
    if is_large_text:
        if contrast_ratio >= 4.5:
            return "AAA"
        elif contrast_ratio >= 3.0:
            return "AA"
        else:
            return "Fail"
    else:
        if contrast_ratio >= 7.0:
            return "AAA"
        elif contrast_ratio >= 4.5:
            return "AA"
        else:
            return "Fail"
