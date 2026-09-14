"""
Problem: Gift Packs
Link: https://www.codechef.com/DSAMONDAY020/problems/GPCK
Date: 2026-09-14
Topic: Math, Greedy
Difficulty: Easy
Approach: Each gift pack needs one notebook and one pen, so the number of
          packs that can be made is limited by whichever quantity (notebooks
          or pens) is smaller. Simply take the minimum of the two inputs.
Time Complexity: O(1)
Space Complexity: O(1)
"""


# --------------------------- Solution ----------------------------------------


def main():
    values = list(map(int, input().split()))
    notebooks, pens = values[0], values[1]
    packs = notebooks if notebooks < pens else pens
    print(packs)

if __name__ == "__main__":
    main()
