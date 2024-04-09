class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printList(self):
        current_node = self.head
        while current_node:
            print("%s" % current_node.data, end=" ")
            current_node = current_node.next


def reverseList(lst):  # Reverse elements in linked list
    prev = None
    current = lst.head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    lst.head = prev


def findMiddle(lst):  # find mid element in LinkedList

    slow_ptr = lst.head  # takes 1 step each iter
    fast_ptr = lst.head  # takes 2 steps
    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    return slow_ptr


# detect if linkedlist has a cycle
def ifCycle(lst):
    slow_ptr = lst.head  # takes 1 step each iter
    fast_ptr = lst.head  # takes 2 steps
    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr == slow_ptr:  # cycle detected
            return True
    return False


def createCycle(lst):
    # create cycle
    current = lst.head
    while current.next:
        current = current.next
    current.next = lst.head


if __name__ == "__main__":
    lst = LinkedList()
    lst.append('1')
    lst.append('2')
    lst.append('3')
    lst.append('4')
    reverseList(lst)
    lst.printList()
    print(findMiddle(lst).data)

    lst = LinkedList()

    print(ifCycle(lst))  # no cycle

    lst2 = LinkedList()
    lst2.append('11')
    lst2.append('23')
    lst2.append('44')
    lst2.append('56')
    createCycle(lst2)
    print(ifCycle(lst2))  # no cycle
