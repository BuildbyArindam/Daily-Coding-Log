/**
 * Problem: Create a Circular Queue
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-circular-queue
 * Date: 2026-09-12
 * Difficulty: Medium
 * Topics: Arrays, Queues, Data Structure Design, Circular Buffer
 *
 * Approach:
 * Fixed-size array backing store with two pointers (read/write) that wrap
 * around using modular indexing (max + 1 = size). `null` marks empty slots,
 * which doubles as both the "full" and "empty" check — enqueue fails if the
 * write slot isn't null, dequeue fails if the read slot is null.
 *
 * Time Complexity: O(1) for enqueue and dequeue
 * Space Complexity: O(n), where n = queue size
 */


// --------------------------- Solution --------------------------------


class CircularQueue {
  constructor(size) {
    this.queue = [];
    this.read = 0;
    this.write = 0;
    this.max = size - 1;
    while (size > 0) {
      this.queue.push(null);
      size--;
    }
  }
  print() {
    return this.queue;
  }
  enqueue(item) {
    if (this.queue[this.write] !== null) {
      return null;
    }
    this.queue[this.write] = item;
    this.write++;
    if (this.write > this.max) {
      this.write = 0;
    }
    return item;
  }
  dequeue() {
    if (this.queue[this.read] === null) {
      return null;
    }
    const item = this.queue[this.read];
    this.queue[this.read] = null;
    this.read++;
    if (this.read > this.max) {
      this.read = 0;
    }
    return item;
  }
}
