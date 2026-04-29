# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the head is null we return it
        if not head:
            return head

        currNode = head
        prevNode = None

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode 
            prevNode = currNode
            currNode = nextNode
        
        return prevNode

        


        

        