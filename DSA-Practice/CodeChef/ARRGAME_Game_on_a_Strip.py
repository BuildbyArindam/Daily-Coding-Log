"""
Platform   : CodeChef
Problem    : Game on a Strip (ARRGAME)
Link       : https://www.codechef.com/problems/ARRGAME
Difficulty : 1705
Topics     : Game Theory, Greedy, Observation, Sorting
Date       : 2026-09-24

Approach:
    Split the array into maximal segments of consecutive zeros. Only the
    lengths of these segments matter, and in practice only the two largest.
      - No zero segments          -> "No"
      - Exactly one segment       -> "Yes" iff its length is odd
      - Two or more segments      -> let L = largest, S = second largest;
                                     "Yes" iff L is odd and 2*S < L + 1
                                     (i.e. the second-largest can't
                                     out-tempo the largest)

Complexity:
    Time  : O(N + K log K), K = number of segments (K <= N)
            (top-two selection instead of sorting would make it O(N))
    Space : O(K) for segment lengths, O(N) for the input array
"""


# ------------------------------------- Solution -------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        segments = []
        cnt = 0
        for x in A:
            if x == 0:
                cnt += 1
            else:
                if cnt > 0:
                    segments.append(cnt)
                    cnt = 0
        if cnt > 0:
            segments.append(cnt)
        if not segments:
            print("No")
        elif len(segments) == 1:
            print("Yes" if segments[0] % 2 == 1 else "No")
        else:
            segments.sort(reverse=True)
            L = segments[0]  
            S = segments[1]  
            if L % 2 == 1 and 2 * S < L + 1:
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    solve()
