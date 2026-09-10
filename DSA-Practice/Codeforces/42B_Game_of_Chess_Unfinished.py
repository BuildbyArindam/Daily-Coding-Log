"""
Problem   : Game of Chess (unfinished)
Link      : https://codeforces.com/problemset/problem/42/B
Platform  : Codeforces
Difficulty: *1700
Topic     : Implementation
Date      : 2026-09-10

Approach:
Given positions of two white rooks, the white king, and the black king,
determine if the black king is currently in checkmate. A square is
"attacked" if it's adjacent to the white king or lies on a rook's
row/column with no blocking piece in between. First check if the black
king's current square is attacked (in check). If not -> "OTHER".
If it is, try all 8 neighboring squares as candidate escape moves for
the black king (skipping squares occupied by the white king, and
removing a rook from the attack list if it would be captured on that
square). If any resulting square is safe -> "OTHER" (king escapes or
captures out of check). If none are safe -> "CHECKMATE".

Complexity:
Time  : O(1) - fixed 8x8 board, at most 8 king moves x 2 rooks x 8 squares to scan
Space : O(1) - constant number of positions stored
"""


# ------------------------------ Solution ------------------------------------


def solve():
    pieces = input().split()
    def pos(s):
        return ord(s[0]) - ord('a'), int(s[1]) - 1
    r1 = pos(pieces[0])
    r2 = pos(pieces[1])
    wk = pos(pieces[2])
    bk = pos(pieces[3])
    rooks = [r1, r2]
    def inside(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def attacked(square, rook_list, king_pos):
        """
        Check whether 'square' is attacked by the white pieces.
        rook_list contains the rooks that still exist.
        """
        x, y = square
        if max(abs(x - king_pos[0]), abs(y - king_pos[1])) == 1:
            return True
        for i, (rx, ry) in enumerate(rook_list):
            if rx != x and ry != y:
                continue
            if rx == x:
                step = 1 if y > ry else -1
                cy = ry + step
                blocked = False
                while cy != y:
                    if (rx, cy) == king_pos:
                        blocked = True
                    for j, other in enumerate(rook_list):
                        if j != i and other == (rx, cy):
                            blocked = True
                    cy += step
                if not blocked:
                    return True
            else:
                step = 1 if x > rx else -1
                cx = rx + step
                blocked = False
                while cx != x:
                    if (cx, ry) == king_pos:
                        blocked = True
                    for j, other in enumerate(rook_list):
                        if j != i and other == (cx, ry):
                            blocked = True
                    cx += step
                if not blocked:
                    return True
        return False
    in_check = attacked(bk, rooks, wk)
    if not in_check:
        print("OTHER")
        return
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx = bk[0] + dx
            ny = bk[1] + dy
            if not inside(nx, ny):
                continue
            new_pos = (nx, ny)
            if new_pos == wk:
                continue
            new_rooks = [r for r in rooks if r != new_pos]
            if not attacked(new_pos, new_rooks, wk):
                print("OTHER")
                return
    print("CHECKMATE")

if __name__ == "__main__":
    solve()
