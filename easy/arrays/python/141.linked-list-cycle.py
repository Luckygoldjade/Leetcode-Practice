#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (52.82%)
# Likes:    16785
# Dislikes: 1523
# Total Accepted:    4.2M
# Total Submissions: 7.9M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
# 
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
# 
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
# 
# 
# 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = ListNode(0) # dummy head
        self.tail = self.head # initially tail is dummy



    def hasCycle(self, head: ListNode) -> bool:
        """
        Use Floyd's Tortoise and Hare algorithm to detect cycle in linked list.
        """
        # the linked list is already created in main()
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    def append(self, val):
        """Append to tail (enqueue style)."""
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

def __repr__(self):
    vals, cur = [], self.head.next  # skip dummy
    visited = set()
    while cur:
        if id(cur) in visited:
            vals.append(f"{cur.val} (cycle)")
            break
        visited.add(id(cur))
        vals.append(str(cur.val))
        cur = cur.next
    return " -> ".join(vals) if vals else "∅"

# @lc code=end

def main():
    # Sentinel head (dummy before first data node)
    # class LinkedListSentinel = Solution

    # Example 1
    head = [3,2,0,-4]
    # Internally, pos is used to denote the index of the node that tail's next pointer is connected
    # to. Note that pos is not passed as a parameter.
    pos = 1
    lls = Solution()
    cycle_start = None  # to save the address of pos node
    pos_cnt = 0
    for v in head: 
        lls.append(v)
        # we know pos beforehand. so save the pos cycle node
        if pos >= 0:
            if pos_cnt == pos:
                cycle_start = lls.tail

            lls.tail.next = cycle_start
        print("Appending:", v, "Tail now:", lls.tail.val, "tail next:", lls.tail.next.val if lls.tail.next else None)
        pos_cnt += 1

    print("\n")
    print("Sentinel:", lls)
    print("Sentinel middle:", lls.hasCycle(lls.head.next))


    # # Example 2
    # head = [1,2]
    # pos = 0
    # lls = Solution()
    # for v in head: 
    #     lls.append(v)
    # print("\n")
    # print("Sentinel:", lls)
    # print("Sentinel middle:", lls.hasCycle(lls.head.next))

    # # Example 3
    # head = [1]
    # pos = -1
    # lls = Solution()
    # for v in head: 
    #     lls.append(v)
    # print("\n")
    # print("Sentinel:", lls)
    # print("Sentinel middle:", lls.hasCycle(lls.head.next).val)

    return

if __name__ == "__main__":
    main()


