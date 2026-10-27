"""
Problem   : Obstacle Course (COURSE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/COURSE
Difficulty: 2017
Date      : 2026-10-27
Topics    : Graphs, MST, Prim's, Kruskal's, Geometry/Math

Approach:
    Model the course as a graph with m + 2 nodes: the m obstacle points,
    the inner circle (radius r) and the outer circle (radius R).
    Edge weights are the gaps between objects:
      - point <-> point : Euclidean distance
      - inner <-> point : dist(point, origin) - r
      - point <-> outer : R - dist(point, origin)
      - inner <-> outer : R - r
    The answer is the minimum possible largest edge on a path from inner
    to outer (a minimax/bottleneck path). Run an O(V^2) Prim-style
    selection where a node's key is max(edge weight, parent's key), and
    stop as soon as the outer node is settled. This is the same value as
    the heaviest edge on the inner-outer path in the MST (Kruskal gives
    the same result).

Complexity (per test case, m = number of points):
    Time  : O(m^2), dense-graph Prim with no heap
    Space : O(m)
"""


# ------------------------------------------------------- Solution -------------------------------------------------------------


import sys
from math import hypot as _h

def _split_cases(_tk, _pos, _cnt):
    _cases = []
    _n = len(_tk)
    try:
        while (_cnt is None and _pos < _n) or (_cnt is not None and len(_cases) < _cnt):
            _r = int(_tk[_pos]); _R = int(_tk[_pos + 1]); _m = int(_tk[_pos + 2])
            _pos += 3
            if _m < 0 or _pos + 2 * _m > _n:
                return None
            _pts = [(int(_tk[_pos + 2 * i]), int(_tk[_pos + 2 * i + 1])) for i in range(_m)]
            _pos += 2 * _m
            _cases.append((_r, _R, _pts))
    except (IndexError, ValueError):
        return None
    return _cases if _pos == _n else None

def _solve(_in, _out, _pts):
    _m = len(_pts)
    _X = [p[0] for p in _pts]
    _Y = [p[1] for p in _pts]
    _D = [_h(a, b) for a, b in _pts]
    _I = _m
    _O = _m + 1
    _tot = _m + 2
    _big = float("inf")
    _val = [_big] * _tot
    _val[_I] = 0.0
    _seen = [False] * _tot
    while True:
        _u = -1
        _bv = _big
        for _k in range(_tot):
            if not _seen[_k] and _val[_k] < _bv:
                _bv = _val[_k]
                _u = _k
        if _u == _O or _u < 0:
            break
        _seen[_u] = True
        if _u == _I:
            for _v in range(_m):
                _w = max(_D[_v] - _in, _bv)
                if _w < _val[_v]:
                    _val[_v] = _w
            _w = max(_out - _in, _bv)
            if _w < _val[_O]:
                _val[_O] = _w
        else:
            _xu, _yu = _X[_u], _Y[_u]
            for _v in range(_m):
                if _seen[_v]:
                    continue
                _w = max(_h(_xu - _X[_v], _yu - _Y[_v]), _bv)
                if _w < _val[_v]:
                    _val[_v] = _w
            _w = max(_D[_u] - _in, _bv)
            if not _seen[_I] and _w < _val[_I]:
                _val[_I] = _w
            _w = max(_out - _D[_u], _bv)
            if _w < _val[_O]:
                _val[_O] = _w
    return _val[_O]

def _go(_s):
    _tk = _s.split()
    if not _tk:
        return ""
    _cs = _split_cases(_tk, 1, int(_tk[0]))   
    if _cs is None:
        _cs = _split_cases(_tk, 0, None) 
    return "\n".join("%.3f" % _solve(r, R, p) for r, R, p in _cs)

if __name__ == "__main__":
    print(_go(sys.stdin.read()))
