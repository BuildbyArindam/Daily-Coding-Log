/**
 * Problem: Insert an Element into a Max Heap
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/insert-an-element-into-a-max-heap
 * Date: 2026-09-17
 * Difficulty: Easy-Medium
 * Topics: Data Structures, Heaps, Binary Tree (Array Representation), Sift-Up
 *
 * Approach:
 * Represent the heap as a 1-indexed array (index 0 unused) so that for
 * any node at index i, its parent is at floor(i/2) and children are at
 * 2i and 2i+1. To insert, push the new element to the end of the array,
 * then "sift up": repeatedly compare it with its parent and swap while
 * it's greater, until the max-heap property is restored or the root
 * is reached.
 *
 * Time Complexity: O(log n) — the element rises at most the height of the heap
 * Space Complexity: O(1) extra space (in-place, excluding input storage)
 */


// ------------------------------- Solution --------------------------------------------


var MaxHeap = function() {
  this.heap = [null];
  this.insert = function(element) {
    this.heap.push(element);
    var index = this.heap.length - 1;
    while (index > 1) {
      var parent = Math.floor(index / 2);
      if (this.heap[index] <= this.heap[parent]) {
        break;
      }
      var temp = this.heap[index];
      this.heap[index] = this.heap[parent];
      this.heap[parent] = temp;
      index = parent;
    }
  };
  this.print = function() {
    return this.heap.slice(1);
  };
};
