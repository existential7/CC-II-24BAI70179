class MyStack(object):

    def __init__(self):
        self.object = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.object.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.object.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.object[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.object) == 0 else False
    def display(self):
        print(self.object)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(["MyStack","push","push","peek","pop","empty"])
obj.push(1)
obj.push(2)
obj.display()
param_2 = obj.top()
obj.display()
param_3 = obj.pop()
param_4 = obj.empty()
print(None, None, None, param_2, param_3, param_4)

