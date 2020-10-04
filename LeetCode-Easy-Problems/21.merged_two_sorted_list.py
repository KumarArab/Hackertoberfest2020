#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        node = ListNode()
        head = node
        finalList = []
        while(l1 != None and l2 != None):
            if(l1.val <= l2.val):
                node.next = ListNode(l1.val,None)
                node = node.next
                finalList.append(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val,None)
                node = node.next
                finalList.append(l2.val)
                l2 = l2.next
        if(l1 != None):
            while(l1 != None):
                node.next = ListNode(l1.val,None)
                node = node.next
                finalList.append(l1.val)
                l1 = l1.next
        elif(l2 != None):
            while(l2 != None):
                node.next = ListNode(l2.val,None)
                node = node.next
                finalList.append(l2.val)
                l2 = l2.next
        return head.next
            