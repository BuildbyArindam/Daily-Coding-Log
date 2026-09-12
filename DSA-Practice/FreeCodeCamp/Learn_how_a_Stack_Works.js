/**
 * Problem: Learn how a Stack Works
 * Platform: freeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/learn-how-a-stack-works
 * Date: 2026-09-12
 * Difficulty: Easy
 * Topics: Stacks, Data Structures
 *
 * Approach:
 * A stack follows LIFO (Last In, First Out) order — only the top element
 * can be accessed at a time. Used built-in array methods to simulate this:
 *   - pop()  removes the last element (top of stack) -> removes "PSY44"
 *   - push() adds a new element to the top -> adds "CS50"
 *
 * Time Complexity: O(1) for both pop() and push() (array end operations)
 * Space Complexity: O(1) additional space (in-place mutation of the array)
 */


// ----------------------------- Solution -------------------------------------


var homeworkStack = ["BIO12","HIS80","MAT122","PSY44"];
// Only change code below this line

homeworkStack.pop();
homeworkStack.push("CS50");
