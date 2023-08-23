class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != cur.next and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next

    def printAll(self) -> None:
        cur = self.left.next
        while cur and cur != self.right:
            print(cur.val)
            cur = cur.next


# obj = LinkedList()
# obj.addAtHead(6)
# obj.addAtHead(12)
# obj.addAtHead(22)
# obj.addAtHead(37)
# obj.deleteAtIndex(1)
# obj.addAtIndex(1, 7)
# obj.addAtTail(81)
# obj.printAll()
