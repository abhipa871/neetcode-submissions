"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_curr = {None:None}
        ptr = head
        while ptr:
            old_to_curr[ptr] = Node(x=ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr:
            old_to_curr[ptr].next = old_to_curr[ptr.next]
            old_to_curr[ptr].random = old_to_curr[ptr.random]
            ptr = ptr.next
        return old_to_curr[head]
