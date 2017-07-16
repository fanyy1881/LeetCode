# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: Li
        1， l1比l2短
        """
        def tarns_node_to_num(node):
            number = 0
            count = 0
            while node:
                number = node.val * (10 ** count) + number
                node = node.next
                count += 1
            return number

        def trans_num_to_node(number):
            node = ListNode(0)
            tmp = node
            while number:
                number, re = divmod(number, 10)
                tmp.val = re
                if number == 0:
                    break
                tmp.next = ListNode(0)
                tmp = tmp.next
            return node

        num1 = (tarns_node_to_num(l1))
        num2 = (tarns_node_to_num(l2))
        num0 = num1 + num2
        l0 = trans_num_to_node(num0)
        return l0

if __name__ == '__main__':
    def get_list_node(in_list):
        if in_list:
            l0 = ListNode(in_list[0])
            tmp = l0
        for val in in_list[1:]:
            tmp.next = ListNode(val)
            tmp = tmp.next
        return l0

    def show_list_node(node):
        while node:
            print(node.val)
            node = node.next

    l1 = get_list_node([1, 1])
    l2 = get_list_node([5])
    l0 = Solution().addTwoNumbers(l1, l2)
    show_list_node(l0)