/*
 * Problem : 1207. Unique Number of Occurrences
 * Link    : https://leetcode.com/problems/unique-number-of-occurrences/
 * Platform: LeetCode
 * Level   : Easy
 * Topics  : Array, Hash Table
 * Date    : 2026-10-03
 *
 * Approach:
 *   1. Count the frequency of each value with a hash map.
 *   2. Walk through the frequencies and track the ones already seen in a
 *      second hash map. If a frequency repeats, two values share the same
 *      occurrence count, so return false.
 *   3. If no frequency repeats, return true.
 *
 * Time Complexity : O(n)  - one pass to count, one pass over distinct values
 * Space Complexity: O(n)  - the maps hold at most n distinct values/frequencies
 */


// ------------------------------------- Solution -------------------------------------------


class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        bool ret = true;
        unordered_map<int, int> tempMap;
        unordered_map<int, int> revereseTempMap;
        
        for (int i = 0; i < arr.size(); ++i) {
            tempMap[arr[i]]++;
        }
        
        unordered_map<int, int>::iterator iter = tempMap.begin();
        unordered_map<int, int>::iterator endIter = tempMap.end();
        
        for (; iter != endIter; ++iter) {
            if (revereseTempMap[iter->second] != 0) {
                ret = false;
                break;
            }
            else {
                revereseTempMap[iter->second] = 1;
            }            
        }

        return ret;
    }
};
