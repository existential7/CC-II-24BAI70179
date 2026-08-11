class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Add element to Stack 1
        self.s1.append(x)

    def dequeue(self):
        """
        :rtype: int
        """
        # If Stack 2 is empty, move all elements
        # from Stack 1 to Stack 2
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())

        # Remove front element
        return self.s2.pop()

    def front(self):
        """
        :rtype: int
        """
        # If Stack 2 is empty, transfer elements
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())

        # Return front element without removing it
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0

    def display(self):
        """
        Display queue elements
        """
        queue = self.s2[::-1] + self.s1
        print(queue)


# Your MyQueue object will be instantiated and called as such:

obj = MyQueue()

print(["MyQueue", "enqueue", "enqueue", "enqueue", "enqueue",
       "front", "dequeue", "empty"])

obj.enqueue(2)
obj.enqueue(43)
obj.enqueue(24)
obj.enqueue(56)

obj.display()

param_2 = obj.front()
param_3 = obj.dequeue()
param_4 = obj.empty()

obj.display()

print(None, None, None, None, param_2, param_3, param_4)