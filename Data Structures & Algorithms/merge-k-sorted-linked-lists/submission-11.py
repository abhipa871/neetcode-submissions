# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeList(self, l1, l2):
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        i=0
        while i+1<len(lists):
            #dummy = node = ListNode()
            list1 = lists[0]
            list2 = lists[i+1]
            lists[0] = self.mergeList(list1, list2)  
            i+=1      
        return lists[0]
