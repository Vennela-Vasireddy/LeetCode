# Last updated: 11/15/2025, 6:25:14 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        copy = result
        value = 0
        buffer = 0
        while l1 and l2:
            value = l1.val+l2.val+buffer
            if(value >=10):
                result.next = ListNode(int(value)%10)
                buffer = int((value)/10)
            else:
                result.next = ListNode(value)
                buffer = 0
            l2 = l2.next
            result = result.next
            l1 = l1.next
            if l1 != None and l2 == None:
                l2 = ListNode()
            if l2 != None and l1 == None:
                l1 = ListNode()
            if(buffer!=0):
                result.next = ListNode(buffer)
        return copy.next   
        