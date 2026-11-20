/*
 * Problem   : 880. Decoded String at Index
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/decoded-string-at-index/
 * Date      : 2026-10-07
 * Difficulty: Medium
 * Topics    : String, Stack
 *
 * Approach  : Length tracking + reverse traversal
 *   1. Forward pass: compute the total decoded length without building the
 *      string (letters add 1, digit d multiplies the length by d).
 *   2. Backward pass: undo each operation.
 *        - Digit d: divide length by d, and reduce k with k %= length
 *          (the decoded string repeats every `length` characters).
 *        - Letter: if k == 0 or k == length, this letter is the answer;
 *          otherwise decrement length.
 *
 * Time      : O(n), two linear passes over the input
 * Space     : O(1), only counters are used (long long avoids overflow)
 */


// ------------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    std::string decodeAtIndex(std::string inputString, int k) {
        long long decodedLength = 0; // Total length of the decoded string
        for (auto character : inputString) {
            if (isdigit(character)) {
                // If the character is a digit, update the decoded length accordingly
                decodedLength *= character - '0';
            } else {
                // If the character is a letter, increment the decoded length
                decodedLength++;
            }
        }

        // Traverse the input string in reverse to decode and find the kth character
        for (int i = inputString.size() - 1; i >= 0; i--) {
            if (isdigit(inputString[i])) {
                // If the character is a digit, adjust the length and k accordingly
                decodedLength /= (inputString[i] - '0');
                k = k % decodedLength;
            } else {
                // If the character is a letter, check if it's the kth character
                if (k == 0 || decodedLength == k)
                    return string("") + inputString[i]; // Return the kth character as a string
                decodedLength--;
            }
        }

        return ""; // Return an empty string if no character is found   
    }
};
