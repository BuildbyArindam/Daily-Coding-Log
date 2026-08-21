"""
Problem: Print Reversed Linked List
Platform: Coding Ninjas / Naukri Code360
Link: https://www.naukri.com/code360/problems/print-reversed-linked-list_564?kunjiRedirection=true
Difficulty: Easy
Date Solved: 2026-08-21

Approach:
Build a singly linked list from input, then print its elements in
reverse order without physically reversing the list. Recursion
naturally unwinds in LIFO order, so recursing to the tail first
and printing on the way back ("post-order" print) yields the
reversed sequence without extra pointer manipulation.

Time Complexity: O(n)  -> each node visited once
Space Complexity: O(n) -> recursion call stack (worst case for
                           skewed/long lists; can hit recursion
                           limits for very large n, hence the
                           setrecursionlimit bump)
"""


# ----------------------------- Solution -----------------------------


from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printReverse(head) :
    if head is None :
        return
    printReverse(head.next)
    print(head.data, end = " ")

def takeInput() :
    head = None
    tail = None
    datas = list(map(int, stdin.readline().rstrip().split(" ")))
    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)
        if head is None :
            head = newNode
            tail = newNode
        else :
            tail.next = newNode
            tail = newNode
        i += 1
    return head

def printLinkedList(head) :
    while head is not None :
        print(head.data, end = " ")
        head = head.next
    print()

t = int(stdin.readline().rstrip())
while t > 0 :
    head = takeInput()
    printReverse(head)
    print()
    t -= 1
