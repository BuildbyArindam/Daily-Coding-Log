/*
 * Problem:    68. Text Justification
 * Platform:   LeetCode 
 * Link:       https://leetcode.com/problems/text-justification/
 * Date:       2026-11-21
 * Difficulty: Hard
 * Topics:     Array, String, Simulation
 *
 * Approach:
 *   Greedy line packing. Add words to the current line while
 *   (chars so far + 1 space per word + next word) fits in maxWidth.
 *   When the next word doesn't fit, distribute the leftover spaces
 *   round-robin across the gaps from left to right, so the leftmost
 *   gaps get the extra space. A line with a single word works out to
 *   left-justified with trailing padding. The last line is always
 *   left-justified: single spaces between words, padded on the right.
 *
 * Complexity:
 *   Time:  O(N * L) -- every word is processed once and each output
 *          line is built in O(maxWidth); N = number of words,
 *          L = maxWidth (equivalently O(total output characters)).
 *   Space: O(maxWidth) auxiliary for the current line, excluding the
 *          output.
 */


// ------------------------------------- Solution ------------------------------------------------------


class Solution {
public:
    std::vector<std::string> fullJustify(std::vector<std::string>& words, int maxWidth) {
        std::vector<std::string> res;

        int i = 0;
        int width = 0;
        std::vector<std::string> curLine;

        while (i < words.size()) {
            std::string curWord = words[i];

            if (width + curWord.length() <= maxWidth) {
                curLine.push_back(curWord);
                width += curWord.length() + 1;
                i++;
            } else {
                int spaces = maxWidth - width + curLine.size();

                int added = 0;
                int j = 0;

                while (added < spaces) {
                    if (j >= curLine.size() - 1) {
                        j = 0;
                    }

                    curLine[j] += " ";
                    added++;
                    j++;
                }

                std::string line = "";
                for (const std::string& word : curLine) {
                    line += word;
                }
                res.push_back(line);

                curLine.clear();
                width = 0;
            }
        }

        for (int word = 0; word < curLine.size() - 1; word++) {
            curLine[word] += " ";
        }
        curLine[curLine.size() - 1] += std::string(maxWidth - width + 1, ' ');

        std::string lastLine = "";
        for (const std::string& word : curLine) {
            lastLine += word;
        }
        res.push_back(lastLine);

        return res;
    }
};
