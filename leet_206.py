# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head):
        """Reverses a singly-linked list
        :type head: ListNode
        :rtype: ListNode
        """

        # Store current node, initialized at head
        if not head == None:
            curr_node = head
            # Store next node, initialized at head.next
            next_node = head.next
            # Store previous node
            prev_node = None
            while curr_node:
                # Get next node
                next_node = curr_node.next
                # Make previous the next node
                curr_node.next = prev_node
                # Set current node as previous
                prev_node = curr_node
                # Move curr node to next_node
                curr_node = next_node
            return prev_node


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    reverse = sol.reverseList(head)
    print(reverse, reverse.next, reverse.next.next)  # 4 3 2
