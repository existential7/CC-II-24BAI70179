class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.move()

        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()

        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def move(self):
        """
        Move elements from stack1 to stack2
        """
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

    def display(self):
        print("Stack1:", self.stack1)
        print("Stack2:", self.stack2)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()

print(["MyQueue", "push", "push", "push", "push", "peek", "pop", "empty"])

obj.push(2)
obj.push(43)
obj.push(24)
obj.push(56)

obj.display()

param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()

obj.display()

print(None, None, None, None, param_2, param_3, param_4)