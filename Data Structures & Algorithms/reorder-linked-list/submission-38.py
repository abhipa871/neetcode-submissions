# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next, second_half = None, slow.next     
        first_half = head
        prev, curr = None, second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second_half = prev
        while  second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            second_half = temp2
            first_half = temp1
        