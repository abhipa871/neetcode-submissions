# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length+=1
        ptr = head
        print(length)
        if length==1:
            return None
        elif length-n-1==-1:
            return head.next
        count=0
        while ptr:
            if count==length-n-1:
                print(count)
                ptr.next = ptr.next.next
            count+=1

            ptr= ptr.next
        return head