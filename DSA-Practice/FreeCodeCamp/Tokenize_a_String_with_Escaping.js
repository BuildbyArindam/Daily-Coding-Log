/**
 * Problem: Tokenize a string with escaping
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/tokenize-a-string-with-escaping
 * Date: 2026-09-05
 * Difficulty: Easy-Medium 
 * Topics: String Manipulation, Parsing, Escaping Logic
 *
 * Approach:
 * Single left-to-right scan with a running "current" token buffer.
 * - If the char is the escape char, blindly consume the NEXT char
 *   as a literal (even if that next char is the separator or the
 *   escape char itself), skipping the normal separator/escape check
 *   for it.
 * - If the char is the separator, close off the current token and
 *   start a new one.
 * - Otherwise, append to the current token.
 * Trailing token (after the last separator) is pushed at the end.
 *
 * Time complexity: O(n) — one pass over the string, each char
 *                   processed at most twice (once as esc, once as
 *                   the escaped char).
 * Space complexity: O(n) — output tokens + the "current" buffer,
 *                    proportional to input length.
 */


// ---------------------------- Solution ---------------------------------------


function tokenize(str, sep, esc) {
  const result = [];
  let current = "";
  for (let i = 0; i < str.length; i++) {
    const ch = str[i];
    if (ch === esc) {
      if (i + 1 < str.length) {
        current += str[i + 1];
        i++; 
      } else {
        current += ch;
      }
    }
    else if (ch === sep) {
      result.push(current);
      current = "";
    }
    else {
      current += ch;
    }
  }
  result.push(current);
  return result;
}
