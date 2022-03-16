# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists. Return the head
# of the merged linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        if list1 == None and list2 != None:
            return list2
        if list1 != None and list2 == None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def main(self):
        list1n3 = ListNode(4)
        list1n2 = ListNode(2, list1n3)
        list1n1 = ListNode(1, list1n2)

        list2n3 = ListNode(4)
        list2n2 = ListNode(3, list2n3)
        list2n1 = ListNode(1, list2n2)

        list3 = self.mergeTwoLists(list1n1, list2n1)
        print(list3)


if __name__ == "__main__":
    Solution().main()
