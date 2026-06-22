
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two halves
        l1 = head
        l2 = slow.next
        slow.next = None   # important: cut first half

        # 3. Reverse second half
        prev, curr = None, l2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev

        # 4. Merge alternating
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
        