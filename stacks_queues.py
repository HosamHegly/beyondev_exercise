from collections import deque


class Stack:
    def __init__(self):
        self.first_queue = deque()
        self.second_queue = deque()

    def push(self, value):
        """push value to first queue"""
        self.first_queue.append(value)

    def pop(self):
        """transfer all values from first queue to second except for last element then pop it and return then switch
        queues"""
        if self.first_queue:
            while len(self.first_queue) > 1:
                self.second_queue.append(self.first_queue.popleft())
            value = self.first_queue.popleft()
            self.first_queue, self.second_queue = self.second_queue, self.first_queue
            return value


class Queue:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def enqueue(self, value):
        """push value to first stack"""
        self.first_stack.append(value)

    def dequeue(self):
        """transfer all values from first stack to second then pop"""
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop() if self.second_stack else None


def isBalanced(str):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in str:
        if char in mapping:
            top_element = stack.pop() if stack else "None"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    # Create a stack instance
    stack = Stack()

    # Push elements into the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Popped element:", stack.pop())
    print("Popped element:", stack.pop())
    print("Popped element:", stack.pop())

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Popped element:", queue.dequeue())
    print("Popped element:", queue.dequeue())
    print("Popped element:", queue.dequeue())


    print(isBalanced("((()))"))  # Output: True
    print(isBalanced("(()"))     # Output: False