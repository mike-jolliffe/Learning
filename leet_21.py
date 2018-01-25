# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def __init__(self):
        self.sortedArray = []
        self.finalLinked = None

    def mergeTwoLists(self, l1, l2):
        """Returns linked list resulting from merging two linked lists in order
           of value
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Make an array of both linked lists
        self.toArray(l1, l2)

        self.finalLinked = ListNode(self.sortedArray.pop(0))
        return self.toLinked(self.sortedArray, self.finalLinked)



    def toArray(self, l1, l2):
        """Returns sorted array of node values"""
        if not l1 is None and not l2 is None:
            self.sortedArray.append(min([l1.val, l2.val]))
            self.sortedArray.append(max([l1.val, l2.val]))
            return self.toArray(l1.next, l2.next)
        elif l1 == None and not l2 is None:
            self.sortedArray.append(l2.val)
            return self.toArray(l1, l2.next)
        elif not l1 is None and l2 == None:
            self.sortedArray.append(l1.val)
            return self.toArray(l1.next, l2)
        else:
            return None

    def toLinked(self, array, linked):
        """Converts an array into a ListNode object"""
        if array:
            linked.next = ListNode(array.pop(0))
            return self.toLinked(array, linked.next)

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    sol = Solution()
    sol.mergeTwoLists(l1, l2)
    print("{} -> {} -> {} -> {} -> {}".format(sol.finalLinked,
    sol.finalLinked.next, sol.finalLinked.next.next, sol.finalLinked.next.next.next,
    sol.finalLinked.next.next.next.next))  # 1 -> 1 -> 2 -> 3 -> 4
