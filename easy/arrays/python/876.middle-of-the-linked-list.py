#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (80.79%)
# Likes:    12652
# Dislikes: 419
# Total Accepted:    2.6M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, return the middle node of the linked
# list.
# 
# If there are two middle nodes, return the second middle node.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we
# return the second one.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(first_data_node: ListNode) -> ListNode:
    """
    Fast/slow pointer technique. When length is even, returns the second middle.
    Time: O(n), Space: O(1)
    """
    slow = fast = first_data_node
    while fast and fast.next:
        slow = slow.next        # moves 1 step
        fast = fast.next.next   # moves 2 steps
    return slow

class Solution:
    """
    Sentinel head (dummy before first data node)
    class LinkedListSentinel
    """
    def __init__(self):
        self.head = ListNode()  # dummy node (no real data)
        self.tail = self.head   # initially points to dummy

    def append(self, val):
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def find_middle(self):
        # Start at the FIRST DATA node = self.head.next
        return middleNode(self.head.next)


    def __repr__(self):
        vals, curr = [], self.head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals) + " -> None"

# @lc code=end







def main():
    # Sentinel head (dummy before first data node)
    # class LinkedListSentinel

    # Example 1
    arr = [1,2,3,4,5]
    lls = Solution()
    for v in arr: lls.append(v)
    mid = lls.find_middle() # -s/b 3
    print("\n")
    print(mid.val)

    # Example 2
    arr = [1,2,3,4,5,6]
    lls = Solution()
    for v in arr: lls.append(v)
    mid = lls.find_middle() # -> node with val 4 (second middle of [3,4])
    print("\n")
    print(mid.val)


    return

if __name__ == "__main__":
    main()
