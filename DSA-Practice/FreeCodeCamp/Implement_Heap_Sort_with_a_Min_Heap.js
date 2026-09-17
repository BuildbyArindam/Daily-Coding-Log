/**
 * Problem: Implement Heap Sort with a Min Heap
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/implement-heap-sort-with-a-min-heap
 * Date: 2026-09-17
 * Difficulty: Medium
 * Topics: Heaps, Min-Heap, Priority Queue, Sorting
 *
 * Approach:
 * Build a MinHeap class supporting insert() (sift-up) and remove() (sift-down,
 * extracts the minimum). Push all elements into the heap, then repeatedly call
 * remove() to pop them out in ascending order, producing a sorted array.
 *
 * Time Complexity:  O(n log n) — n inserts at O(log n) each, n removes at O(log n) each
 * Space Complexity: O(n) — heap array storage + O(n) output array
 */


// ------------------------------- Solution -----------------------------------------


function isSorted(a){
  for(let i = 0; i < a.length - 1; i++)
    if(a[i] > a[i + 1])
      return false;
  return true;
}
function createRandomArray(size = 5){
  let a = new Array(size);
  for(let i = 0; i < size; i++)
    a[i] = Math.floor(Math.random() * 100);
  return a;
}
const array = createRandomArray(25);
var MinHeap = function() {
  this.heap = [];
  this.insert = function(value) {
    this.heap.push(value);
    let index = this.heap.length - 1;
    while(index > 0) {
      let parentIndex = Math.floor((index - 1) / 2);
      if(this.heap[parentIndex] <= this.heap[index])
        break;
      [this.heap[parentIndex], this.heap[index]] =
        [this.heap[index], this.heap[parentIndex]];
      index = parentIndex;
    }
  };
  this.remove = function() {
    if(this.heap.length === 0)
      return undefined;
    if(this.heap.length === 1)
      return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    let index = 0;
    while(true) {
      let left = 2 * index + 1;
      let right = 2 * index + 2;
      let smallest = index;
      if(left < this.heap.length &&
         this.heap[left] < this.heap[smallest]) {
        smallest = left;
      }
      if(right < this.heap.length &&
         this.heap[right] < this.heap[smallest]) {
        smallest = right;
      }
      if(smallest === index)
        break;
      [this.heap[index], this.heap[smallest]] =
        [this.heap[smallest], this.heap[index]];
      index = smallest;
    }
    return min;
  };
  this.sort = function() {
    const sorted = [];
    while(this.heap.length > 0) {
      sorted.push(this.remove());
    }
    return sorted;
  };
};
