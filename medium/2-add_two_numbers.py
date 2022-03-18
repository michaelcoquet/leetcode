# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list_temp = self
        list_str = ""
        if list_temp != None:
            list_str = list_str + str(list_temp.val) + " "
            list_temp = list_temp.next
        while 1:
            if list_temp == None:
                break
            list_str = list_str + str(list_temp.val) + " "
            list_temp = list_temp.next

        return list_str


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = False

        prehead = ListNode(-1)
        prev = prehead
        while 1:
            if l1 == None and l2 == None:
                if carry:
                    prev.next = ListNode(1)
                    prev = prev.next
                    return prehead.next
                else:
                    return prehead.next
            elif l1 == None and l2 != None:
                if carry:
                    prev.next = l2
                    if l2.val + 1 >= 10:
                        temp_num = l2.val + 1
                        prev.next.val = temp_num % 10
                        carry = True
                    else:
                        prev.next.val = l2.val + 1
                        carry = False
                    prev = prev.next
                    l2 = l2.next
                else:
                    prev.next = l2
                    prev = prev.next
                    return prehead.next
            elif l1 != None and l2 == None:
                if carry:
                    prev.next = l1
                    if l1.val + 1 >= 10:
                        temp_num = l1.val + 1
                        prev.next.val = temp_num % 10
                        carry = True
                    else:
                        prev.next.val = l1.val + 1
                        carry = False
                    prev = prev.next
                    l1 = l1.next
                else:
                    prev.next = l1
                    prev = prev.next
                    return prehead.next
            else:
                if carry:
                    if l1.val + l2.val + 1 >= 10:
                        temp_num = l1.val + l2.val + 1
                        prev.next = l1
                        prev.next.val = temp_num % 10
                        prev = prev.next
                        carry = True
                    else:
                        prev.next = l1
                        prev.next.val = l1.val + l2.val + 1
                        prev = prev.next
                        carry = False
                else:
                    if l1.val + l2.val >= 10:
                        temp_num = l1.val + l2.val
                        prev.next = l1
                        prev.next.val = temp_num % 10
                        prev = prev.next
                        carry = True
                    else:
                        prev.next = l1
                        prev.next.val = l1.val + l2.val
                        prev = prev.next
                        carry = False

                l1 = l1.next
                l2 = l2.next

        return prehead.next

    def makeList(self, nums) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead
        for digit in nums:
            prev.next = ListNode(digit)
            prev = prev.next
        return prehead.next

    def main(self):
        l1 = [2, 4, 9]
        l2 = [5, 6, 4, 9]
        l1_linked = self.makeList(l1)
        l2_linked = self.makeList(l2)
        print(l1_linked)
        print(l2_linked)

        list3 = self.addTwoNumbers(l1_linked, l2_linked)
        print(list3)


if __name__ == "__main__":
    Solution().main()
