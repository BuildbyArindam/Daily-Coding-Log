


# ------------------------ Solution -------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    A = data[0]
    B = data[1]
    n = len(A)
    L_min = -1
    R_max = -1
    for i in range(n):
        if A[i] != B[i]:
            if L_min == -1:
                L_min = i
            R_max = i
    sub_A = A[L_min:R_max + 1]
    sub_B = B[L_min:R_max + 1]
    if sub_A[::-1] != sub_B:
        print(0)
        return
    valid_count = 1  
    l = L_min - 1
    r = R_max + 1
    while l >= 0 and r < n:
        if A[l] == B[r] and A[r] == B[l]:
            valid_count += 1
            l -= 1
            r += 1
        else:
            break
    print(valid_count)

if __name__ == '__main__':
    solve()
