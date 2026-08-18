/*
 * Problem   : Red-Green Tower (RGTWR)
 * Link      : https://www.codechef.com/problems/RGTWR
 * Date      : 2026-08-18
 * Topics    : Dynamic Programming, 0/1 Knapsack, Subset Sum, Combinatorics, Greedy
 * Difficulty: Medium
 *
 * Approach:
 *   1. Find the maximum tower height h such that h*(h+1)/2 <= (R+G),
 *      i.e., the largest triangular number of blocks affordable.
 *   2. Each level i (1..h) uses i blocks, all one color. Assigning a
 *      subset of levels to be "red" is equivalent to a 0/1 knapsack:
 *      count subsets of {1,...,h} whose sum (red block count) lies in
 *      the valid range [totalBlocks - G, R], since the rest must be
 *      coverable by green blocks.
 *   3. DP: ways[s] = number of subsets of level-sizes summing to s,
 *      computed via standard 0/1 knapsack (iterate items, inner loop
 *      descending to avoid reuse). Sum ways[] over the valid range.
 *
 * Complexity:
 *   Time : O(h * upperBound)  ~ O(budget^1.5) worst case, h = O(sqrt(budget))
 *   Space: O(upperBound)
 */


// ------------------------ Solution -------------------------------------


#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1000000007LL;

long long findMaxHeight(long long budget) {
    long long lvl = 0;
    while ((lvl + 1) * (lvl + 2) / 2 <= budget) lvl++;
    return lvl;
}

int main() {
    long long redCount, greenCount;
    cin >> redCount >> greenCount;
    long long budget = redCount + greenCount;
    long long height = findMaxHeight(budget);
    long long totalBlocks = height * (height + 1) / 2;
    long long lowerBound = max(0LL, totalBlocks - greenCount);
    long long upperBound = min(redCount, totalBlocks);
    vector<long long> ways(upperBound + 1, 0LL);
    ways[0] = 1LL;
    long long usableItems = min(height, upperBound);
    for (long long piece = 1; piece <= usableItems; piece++) {
        for (long long s = upperBound; s >= piece; s--) {
            long long add = ways[s - piece];
            if (add) {
                ways[s] += add;
                if (ways[s] >= MOD) ways[s] -= MOD;
            }
        }
    }
    long long result = 0;
    for (long long s = lowerBound; s <= upperBound; s++) {
        result += ways[s];
        if (result >= MOD) result -= MOD;
    }
    cout << result << "\n";
    return 0;
}
