/**
 * Problem: Inventory Update
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update
 * Date: 2026-09-11
 * Difficulty: Easy–Medium
 * Topics: Arrays, Linear Search, Sorting
 *
 * Approach:
 * For each item in the new inventory (arr2), linearly search the current
 * inventory (arr1) for a matching item name. If found, add the new quantity
 * to the existing one. If not found, push the new item as-is. Finally,
 * sort arr1 alphabetically by item name.
 *
 * Time Complexity: O(n * m) — n = arr2.length, m = arr1.length, due to the
 *                  nested linear search — plus O(k log k) for the final sort
 *                  (k = length of merged array).
 * Space Complexity: O(1) extra space (updates/pushes happen in place on arr1;
 *                  sort's auxiliary space depends on engine implementation).
 */


// ------------------------ Solution -------------------------------------


function updateInventory(arr1, arr2) {
    for (var i = 0; i < arr2.length; i++) {
        var newItem = arr2[i][1];
        var newQuantity = arr2[i][0];
        var found = false;
        for (var j = 0; j < arr1.length; j++) {
            if (arr1[j][1] === newItem) {
                arr1[j][0] += newQuantity;
                found = true;
                break;
            }
        }
        if (!found) {
            arr1.push([newQuantity, newItem]);
        }
    }
    arr1.sort(function(a, b) {
        return a[1].localeCompare(b[1]);
    });
    return arr1;
}
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];
var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
