/**
 * Problem: Typed Arrays
 * Platform: FreeCodeCamp - Coding Interview Prep / Data Structures
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/typed-arrays
 * Date: 2026-09-12
 * Difficulty: Easy
 * Topics: Arrays, Typed Arrays / ArrayBuffer, Memory Management, Binary Data
 *
 * Approach:
 * Create a raw binary data buffer (ArrayBuffer) of 64 bytes, then create
 * a typed array view (Int32Array) over that buffer to read/write it as
 * 32-bit integers. This demonstrates the two-part typed array model:
 * the buffer (raw memory) and the view (interpretation of that memory).
 *
 * Time Complexity: O(1) - fixed-size allocation and view creation
 * Space Complexity: O(n) - n = buffer byte length (64 bytes here)
 */


// -------------------------- Solution ------------------------------------


var buffer = new ArrayBuffer(64);
var i32View = new Int32Array(buffer);
