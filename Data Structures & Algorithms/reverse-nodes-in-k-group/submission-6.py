class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev_group_tail = ListNode(0, head)
        first_half = head

        while first_half:
            left = first_half
            k_th = k

            while k_th > 1 and left:
                left = left.next
                k_th -= 1
            if not left:
                break
            left.next, second_half = None, left.next
            prev, curr = None, first_half
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev_group_tail.next = prev          # connect previous part to reversed head
            first_half.next = second_half        # old head is now tail, connect to next part

            # Move pointers forward
            prev_group_tail = first_half
            first_half = second_half

        return dummy.next