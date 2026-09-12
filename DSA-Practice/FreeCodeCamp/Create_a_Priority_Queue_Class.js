/**
 * Problem: Create a Priority Queue Class
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-priority-queue-class
 * Date: 2026-09-12
 * Difficulty: Medium
 * Topics: Data Structures, Queues, Priority Queue, Arrays
 *
 * Approach:
 * Implemented a priority queue backed by a plain array of [value, priority]
 * pairs, kept in sorted order by priority. enqueue() finds the correct
 * insertion index via linear scan and splices the item in; dequeue()
 * removes and returns the front element's value.
 *
 * Time Complexity:
 *   enqueue: O(n) — linear scan + splice for insertion
 *   dequeue: O(n) — shift() re-indexes the array
 *   front / size / isEmpty: O(1)
 * Space Complexity: O(n) — stores all n elements in the collection array
 */


// ------------------------------ Solution --------------------------------


function PriorityQueue () {
  this.collection = [];
  this.printCollection = function() {
    console.log(this.collection);
  };
  this.enqueue = function(item) {
    if (this.collection.length === 0) {
      this.collection.push(item);
    } else {
      let added = false;
      for (let i = 0; i < this.collection.length; i++) {
        if (item[1] < this.collection[i][1]) {
          this.collection.splice(i, 0, item);
          added = true;
          break;
        }
      }
      if (!added) {
        this.collection.push(item);
      }
    }
  };
  this.dequeue = function() {
    if (this.collection.length === 0) {
      return undefined;
    }
    return this.collection.shift()[0];
  };
  this.size = function() {
    return this.collection.length;
  };
  this.front = function() {
    if (this.collection.length === 0) {
      return undefined;
    }
    return this.collection[0][0];
  };
  this.isEmpty = function() {
    return this.collection.length === 0;
  };
}
