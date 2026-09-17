/**
 * Problem: Remove an Element from a Max Heap
 * Platform: freeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/remove-an-element-from-a-max-heap
 * Date: 2026-09-17
 * Difficulty: Medium
 * Topics: Heaps, Priority Queues, Arrays, Heapify-Down
 *
 * Approach:
 * Implement a MaxHeap backed by an array. `remove()` extracts the max
 * (root), moves the last element to the root to preserve a complete
 * tree, then sifts it down by repeatedly swapping with the larger
 * child until the heap property is restored.
 *
 * Time Complexity:
 *   - insert: O(log n)   — heapify-up
 *   - remove: O(log n)   — heapify-down
 * Space Complexity: O(1) extra (in-place array), O(n) for heap storage
 */


// ------------------------------------ Solution ---------------------------------------


const MaxHeap = function () {
  this.heap = [];
  this.parent = index => {
    return Math.floor((index - 1) / 2);
  };
  this.insert = element => {
    this.heap.push(element);
    this.heapifyUp(this.heap.length - 1);
  };
  this.heapifyUp = index => {
    let currentIndex = index,
      parentIndex = this.parent(currentIndex);
    while (currentIndex > 0 && this.heap[currentIndex] > this.heap[parentIndex]) {
      this.swap(currentIndex, parentIndex);
      currentIndex = parentIndex;
      parentIndex = this.parent(parentIndex);
    }
  };
  this.swap = (index1, index2) => {
    [this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]];
  };
  this.print = () => {
    return this.heap;
  };
  this.remove = () => {
    if (this.heap.length === 0) {
      return undefined;
    }
    const max = this.heap[0];
    const last = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = last;
      let currentIndex = 0;
      while (true) {
        const leftChild = 2 * currentIndex + 1;
        const rightChild = 2 * currentIndex + 2;
        let largest = currentIndex;
        if (
          leftChild < this.heap.length &&
          this.heap[leftChild] > this.heap[largest]
        ) {
          largest = leftChild;
        }
        if (
          rightChild < this.heap.length &&
          this.heap[rightChild] > this.heap[largest]
        ) {
          largest = rightChild;
        }
        if (largest === currentIndex) {
          break;
        }
        this.swap(currentIndex, largest);
        currentIndex = largest;
      }
    }
    return max;
  };
};
