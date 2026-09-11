"""
Problem   : BerPaint
Link      : https://codeforces.com/problemset/problem/44/F
Platform  : Codeforces
Difficulty: *2700
Topics    : Geometry, Graphs, Planar Arrangement / Union-Find, Flood Fill
Date      : 2026-09-11

Approach:
  - Extend every painted segment to a full line, normalize each line's
    equation (A, B, C) to a canonical integer form so identical lines
    collapse to one key.
  - Build the planar arrangement formed by these lines inside the
    W x H rectangle: intersect every pair of lines, intersect each
    line with the rectangle boundary, and add the rectangle's own
    edges. Use exact Fraction arithmetic throughout to avoid
    precision errors.
  - Sort points along each line/boundary edge to produce arrangement
    edges, marking which sub-segments are "black" (drawn) vs blank,
    and which lie on the outer rectangle boundary.
  - Use the standard half-edge (doubly connected edge list) technique:
    sort outgoing half-edges around each vertex by polar angle,
    compute face traversal via next-half-edge, and compute signed
    area per face (shoelace formula) to find the outer face.
  - Merge faces that are NOT separated by a black or boundary edge
    with Union-Find -> these merged groups are the actual paint
    "regions" a flood fill can spread across.
  - Build a graph over {regions, real (black) edges, real vertices}
    so that a fill started at a boundary point (on an edge/vertex)
    correctly spreads across all region faces touching it, and
    perform BFS/DFS flood fill per query, updating colors in place.
  - Answer by summing region areas per final color.

Complexity (n = segments, m = queries, T = n + m):
  Time : O(T^2) to build the line arrangement (pairwise intersections
         + per-line sorting), plus O(m * (V + E)) worst case for the
         flood-fill BFS/DFS across queries, where V, E = O(T^2).
  Space: O(T^2) for arrangement vertices/edges and the region graph.
"""


# ------------------------------ Solution ---------------------------------------


import sys
from fractions import Fraction
from math import gcd
from functools import cmp_to_key

def norm_line(p, q):
    """Normalized integer equation A*x + B*y + C = 0."""
    x1, y1 = p
    x2, y2 = q
    A = y1 - y2
    B = x2 - x1
    C = -(A * x1 + B * y1)
    g = gcd(abs(A), abs(B))
    A //= g
    B //= g
    C //= g
    if A < 0 or (A == 0 and B < 0):
        A = -A
        B = -B
        C = -C
    return A, B, C

def line_intersection(l1, l2, W, H):
    A1, B1, C1 = l1
    A2, B2, C2 = l2
    D = A1 * B2 - A2 * B1
    if D == 0:
        return None
    x = Fraction(B1 * C2 - B2 * C1, D)
    y = Fraction(A2 * C1 - A1 * C2, D)
    if 0 <= x <= W and 0 <= y <= H:
        return x, y
    return None

def boundary_points(line, W, H):
    """Intersections of a line with the rectangle boundary."""
    A, B, C = line
    ans = set()
    if B != 0:
        for x in (Fraction(0), Fraction(W)):
            y = -(A * x + C) / B
            if 0 <= y <= H:
                ans.add((x, y))
    if A != 0:
        for y in (Fraction(0), Fraction(H)):
            x = -(B * y + C) / A
            if 0 <= x <= W:
                ans.add((x, y))
    return ans

def cmp_dir(a, b):
    """Compare two integer direction vectors by polar angle CCW."""
    ax, ay = a
    bx, by = b
    ha = 0 if (ay > 0 or (ay == 0 and ax >= 0)) else 1
    hb = 0 if (by > 0 or (by == 0 and bx >= 0)) else 1
    if ha != hb:
        return -1 if ha < hb else 1
    cross = ax * by - ay * bx
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0

def solve(W, H, segments, queries):
    line_segments = {}
    for p, q in segments:
        line = norm_line(p, q)
        line_segments.setdefault(line, []).append((p, q))
    for x, y, _ in queries:
        line_segments.setdefault((1, 0, -x), [])
    lines = list(line_segments.keys())
    line_points = {
        line: set(boundary_points(line, W, H))
        for line in lines
    }
    for p, q in segments:
        line = norm_line(p, q)
        line_points[line].add((Fraction(p[0]), Fraction(p[1])))
        line_points[line].add((Fraction(q[0]), Fraction(q[1])))
    for x, y, _ in queries:
        line = (1, 0, -x)
        line_points[line].add((Fraction(x), Fraction(y)))
    L = len(lines)
    for i in range(L):
        for j in range(i):
            p = line_intersection(lines[i], lines[j], W, H)
            if p is not None:
                line_points[lines[i]].add(p)
                line_points[lines[j]].add(p)
    vertex_id = {}
    vx = []
    vy = []
    def get_vertex(p):
        if p not in vertex_id:
            vertex_id[p] = len(vx)
            vx.append(p[0])
            vy.append(p[1])
        return vertex_id[p]
    edges = []
    for line in lines:
        A, B, C = line
        pts = list(line_points[line])
        if B == 0:
            pts.sort(key=lambda p: p[1])
        else:
            pts.sort(key=lambda p: p[0])
        ranges = []
        for p, q in line_segments[line]:
            idx = 1 if B == 0 else 0
            a = min(p[idx], q[idx])
            b = max(p[idx], q[idx])
            ranges.append((a, b))
        ranges.sort()
        merged = []
        for a, b in ranges:
            if not merged or a > merged[-1][1]:
                merged.append([a, b])
            else:
                merged[-1][1] = max(merged[-1][1], b)
        ptr = 0
        if B != 0:
            sgn = 1 if B > 0 else -1
            base_dir = (sgn * B, sgn * (-A))
        else:
            base_dir = (0, 1)
        for i in range(len(pts) - 1):
            p = pts[i]
            q = pts[i + 1]
            u = get_vertex(p)
            v = get_vertex(q)
            t1 = p[1] if B == 0 else p[0]
            t2 = q[1] if B == 0 else q[0]
            a = min(t1, t2)
            b = max(t1, t2)
            while ptr < len(merged) and merged[ptr][1] < a:
                ptr += 1
            is_black = (
                ptr < len(merged)
                and merged[ptr][0] <= a
                and b <= merged[ptr][1]
            )
            edges.append([u, v, is_black, False, base_dir])
    corners = [
        (Fraction(0), Fraction(0)),
        (Fraction(W), Fraction(0)),
        (Fraction(W), Fraction(H)),
        (Fraction(0), Fraction(H)),
    ]
    for side in range(4):
        p0 = corners[side]
        p1 = corners[(side + 1) % 4]
        pts = {p0, p1}
        for A, B, C in lines:
            if side == 0:      
                if A != 0:
                    x = Fraction(-C, A)
                    if 0 <= x <= W:
                        pts.add((x, Fraction(0)))
            elif side == 1:    
                if B != 0:
                    y = Fraction(-(A * W + C), B)
                    if 0 <= y <= H:
                        pts.add((Fraction(W), y))
            elif side == 2:     
                if A != 0:
                    x = Fraction(-(B * H + C), A)
                    if 0 <= x <= W:
                        pts.add((x, Fraction(H)))
            else:              
                if B != 0:
                    y = Fraction(-C, B)
                    if 0 <= y <= H:
                        pts.add((Fraction(0), y))
        if side in (0, 2):
            pts = sorted(pts, key=lambda p: p[0])
        else:
            pts = sorted(pts, key=lambda p: p[1])
        for a, b in zip(pts, pts[1:]):
            u = get_vertex(a)
            v = get_vertex(b)
            dx = 1 if b[0] > a[0] else -1 if b[0] < a[0] else 0
            dy = 1 if b[1] > a[1] else -1 if b[1] < a[1] else 0
            edges.append([u, v, False, True, (dx, dy)])
    E = len(edges)
    V = len(vx)
    outgoing = [[] for _ in range(V)]
    for eid, e in enumerate(edges):
        u, v = e[0], e[1]
        outgoing[u].append(2 * eid)  
        outgoing[v].append(2 * eid + 1) 
    def half_dir(h):
        base = edges[h // 2][4]
        if h & 1:
            return -base[0], -base[1]
        return base
    for v in range(V):
        outgoing[v].sort(
            key=cmp_to_key(lambda a, b: cmp_dir(half_dir(a), half_dir(b)))
        )
    pos = [0] * (2 * E)
    for v in range(V):
        for i, h in enumerate(outgoing[v]):
            pos[h] = i
    destination = [0] * (2 * E)
    for eid, e in enumerate(edges):
        u, v = e[0], e[1]
        destination[2 * eid] = v
        destination[2 * eid + 1] = u
    nxt = [0] * (2 * E)
    for h in range(2 * E):
        v = destination[h]
        nxt[h] = outgoing[v][(pos[h ^ 1] - 1) % len(outgoing[v])]
    face_of_half = [-1] * (2 * E)
    face_area = []
    for start in range(2 * E):
        if face_of_half[start] != -1:
            continue
        fid = len(face_area)
        area2 = 0.0
        h = start
        while face_of_half[h] == -1:
            face_of_half[h] = fid
            e = edges[h // 2]
            if (h & 1) == 0:
                a, b = e[0], e[1]
            else:
                a, b = e[1], e[0]

            area2 += float(
                vx[a] * vy[b] - vy[a] * vx[b]
            )
            h = nxt[h]
        face_area.append(area2 * 0.5)
    outer_face = min(
        range(len(face_area)),
        key=face_area.__getitem__
    )
    F = len(face_area)
    parent = list(range(F))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for eid, e in enumerate(edges):
        is_black = e[2]
        is_boundary = e[3]
        if is_black or is_boundary:
            continue
        a = find(face_of_half[2 * eid])
        b = find(face_of_half[2 * eid + 1])
        if a != b:
            parent[b] = a
    outer_root = find(outer_face)
    root_to_region = {}
    region_of_face = [-1] * F
    region_area = []
    for f in range(F):
        r = find(f)
        if r == outer_root:
            continue
        rid = root_to_region.get(r)
        if rid is None:
            rid = len(region_area)
            root_to_region[r] = rid
            region_area.append(0.0)
        region_of_face[f] = rid
        region_area[rid] += face_area[f]
    R = len(region_area)
    real_edges = [
        eid
        for eid, e in enumerate(edges)
        if e[2] and not e[3]
    ]
    physical_vertices = set()
    for eid in real_edges:
        physical_vertices.add(edges[eid][0])
        physical_vertices.add(edges[eid][1])
    physical_index = {
        v: i
        for i, v in enumerate(physical_vertices)
    }
    edge_count = len(real_edges)
    vertex_count = len(physical_vertices)
    total_nodes = R + edge_count + vertex_count
    graph = [[] for _ in range(total_nodes)]
    left_region = [-1] * E
    right_region = [-1] * E
    for eid in range(E):
        left_region[eid] = region_of_face[face_of_half[2 * eid]]
        right_region[eid] = region_of_face[face_of_half[2 * eid + 1]]
    for k, eid in enumerate(real_edges):
        edge_node = R + k
        lr = left_region[eid]
        rr = right_region[eid]
        if lr >= 0:
            graph[edge_node].append(lr)
            graph[lr].append(edge_node)
        if rr >= 0 and rr != lr:
            graph[edge_node].append(rr)
            graph[rr].append(edge_node)
        u = edges[eid][0]
        v = edges[eid][1]
        for p in (u, v):
            vertex_node = (
                R + edge_count + physical_index[p]
            )
            graph[edge_node].append(vertex_node)
            graph[vertex_node].append(edge_node)
    starts = []
    for x, y, _ in queries:
        p = (Fraction(x), Fraction(y))
        v = vertex_id[p]
        if v in physical_index:
            starts.append(
                R + edge_count + physical_index[v]
            )
        else:
            h = outgoing[v][0]
            eid = h // 2
            starts.append(left_region[eid])
    initial_colors = [0] * R + [1] * (edge_count + vertex_count)
    return region_area, graph, initial_colors, starts

def main():
    input = sys.stdin.buffer.readline
    W, H = map(int, input().split())
    n = int(input())
    segments = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        segments.append(((x1, y1), (x2, y2)))
    m = int(input())
    queries = []
    for _ in range(m):
        x, y, color = input().split()
        queries.append((int(x), int(y), color.decode()))
    region_area, graph, node_color, starts = solve(
        W, H, segments, queries
    )
    R = len(region_area)
    color_id = {
        "white": 0,
        "black": 1
    }
    color_name = [
        "white",
        "black"
    ]
    for start, (_, _, name) in zip(starts, queries):
        if name not in color_id:
            color_id[name] = len(color_name)
            color_name.append(name)
        new_color = color_id[name]
        old_color = node_color[start]
        if old_color == new_color:
            continue
        stack = [start]
        node_color[start] = new_color
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if node_color[v] == old_color:
                    node_color[v] = new_color
                    stack.append(v)
    area_by_color = {}
    for i, c in enumerate(node_color[:R]):
        area_by_color[c] = (
            area_by_color.get(c, 0.0) + region_area[i]
        )
    present = set(node_color)
    answer = []
    for c in present:
        answer.append(
            f"{color_name[c]} {area_by_color.get(c, 0.0):.8f}"
        )
    sys.stdout.write("\n".join(answer))

if __name__ == "__main__":
    main()
