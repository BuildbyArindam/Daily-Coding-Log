/**
 * Problem: Create a Trie Search Tree
 * Platform: FreeCodeCamp — Coding Interview Prep / Data Structures
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-trie-search-tree
 * Date Solved: 2026-09-17
 * Difficulty: Medium 
 * Topics: Trie (Prefix Tree), Tree Data Structures, Hash Map, Recursion, String Processing
 *
 * Approach:
 * Implemented a Trie (prefix tree) using a Node constructor with a Map
 * for children (`keys`) and an `end` flag marking complete words.
 *  - add(word): walks/creates nodes letter by letter, marks the last node as end.
 *  - isWord(word): walks the trie; returns false on any missing letter,
 *    otherwise returns whether the final node is marked as a word end.
 *  - print(): DFS traversal collecting all complete words via prefix accumulation.
 *
 * Time Complexity:
 *  - add:     O(L)        where L = length of the word
 *  - isWord:  O(L)
 *  - print:   O(N)        where N = total number of characters across all stored words
 *
 * Space Complexity: O(N) — one node per unique character path in the trie
 */


// ----------------------------- Solution -----------------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
var Node = function() {
  this.keys = new Map();
  this.end = false;
  this.setEnd = function() {
    this.end = true;
  };
  this.isEnd = function() {
    return this.end;
  };
};
var Trie = function() {
  var root = new Node();
  this.add = function(word) {
    var current = root;
    for (var i = 0; i < word.length; i++) {
      var letter = word[i];
      if (!current.keys.has(letter)) {
        current.keys.set(letter, new Node());
      }
      current = current.keys.get(letter);
    }
    current.setEnd();
  };
  this.isWord = function(word) {
    var current = root;
    for (var i = 0; i < word.length; i++) {
      var letter = word[i];
      if (!current.keys.has(letter)) {
        return false;
      }
      current = current.keys.get(letter);
    }
    return current.isEnd();
  };
  this.print = function() {
    var words = [];
    function search(node, prefix) {
      if (node.isEnd()) {
        words.push(prefix);
      }
      node.keys.forEach(function(child, letter) {
        search(child, prefix + letter);
      });
    }
    search(root, "");
    return words;
  };
};
