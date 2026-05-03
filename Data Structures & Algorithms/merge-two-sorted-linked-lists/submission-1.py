# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # we want a dummy node to start our comparisons
        # we want 2 pointers to keep track of where we are in the 2 linkedlists

        dummy = ListNode(-1)

        curr_val_list1 = list1
        curr_val_list2 = list2
        curr_tail = dummy


        # while both lists are not empty
        while curr_val_list1 and curr_val_list2:

            # grab the smaller value of the two and attach it to the end of the new linked list
            if curr_val_list1.val <= curr_val_list2.val:
                curr_tail.next = curr_val_list1

                # move forward onto the next node in the list
                curr_val_list1 = curr_val_list1.next
            else:
                curr_tail.next = curr_val_list2

                # move forward onto the next node in the list
                curr_val_list2 = curr_val_list2.next

            curr_tail = curr_tail.next # set our tail to the added value 


        # if one of the lists still has nodes just attach it to the tail. 
        if curr_val_list1:
            curr_tail.next = curr_val_list1
        else:            
            curr_tail.next = curr_val_list2


        return dummy.next
        