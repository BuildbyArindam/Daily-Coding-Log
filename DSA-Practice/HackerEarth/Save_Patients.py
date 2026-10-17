"""
Problem   : Save Patients
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/save-patients/
Date      : 2026-10-17
Difficulty: Easy
Topics    : Sorting, Greedy

Approach  : Greedy + sorting. Sort vaccines and patients in ascending order,
            then pair the i-th weakest vaccine with the i-th weakest patient.
            If every vaccine strictly exceeds its paired patient's value,
            all patients can be saved ("Yes"); otherwise "No".

Complexity: Time  O(n log n) for the two sorts
            Space O(n) for the input lists
"""


# ---------------------------------------------- Solution -----------------------------------------------------


n = int(input())
vaccines = list(map(int, input().split()))
patients = list(map(int, input().split()))
vaccines.sort()
patients.sort()
if all(vaccines[i] > patients[i] for i in range(n)):
    print("Yes")
else:
    print("No")
