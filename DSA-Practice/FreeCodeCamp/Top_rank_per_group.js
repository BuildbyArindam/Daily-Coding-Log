/**
 * Problem: Top Rank Per Group
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/top-rank-per-group
 * Date: 2026-09-13
 * Difficulty: Medium
 * Topics: Hashing / Grouping, Sorting, Arrays
 *
 * Approach:
 * Group all records by `groupName` into a hash map, then for each group,
 * sort a copy of its items by `rankName` in descending order and take
 * the top `n` entries. Groups are returned in alphabetical order of the
 * group key.
 *
 * Time Complexity: O(N log N) — dominated by sorting items within each
 * group (worst case one group holds all N items); grouping itself is O(N).
 * Space Complexity: O(N) — for the group hash map and the sorted copies.
 */


// --------------------------- Solution ---------------------------------


function topRankPerGroup(n, data, groupName, rankName) {
  if (n < 0) {
    return undefined;
  }
  const groups = {};
  data.forEach(function (item) {
    const group = item[groupName];
    if (!groups[group]) {
      groups[group] = [];
    }
    groups[group].push(item);
  });
  const sortedGroups = Object.keys(groups).sort();
  return sortedGroups.map(function (group) {
    return groups[group]
      .slice()
      .sort(function (a, b) {
        return b[rankName] - a[rankName];
      })
      .slice(0, n);
  });
}
