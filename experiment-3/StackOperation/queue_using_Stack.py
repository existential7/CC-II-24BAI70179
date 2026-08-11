class MyQueue(object):

    def __init__(self):
        self.object = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.object.append(x)
    

    def pop(self):
        """
        :rtype: int
        """
        return self.object.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.object[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.object) == 0 else False
    
    def display(self):
        print(self.object)
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(["MyQueue","push","push","peek","pop","empty"])
obj.push(2)
obj.push(43)
obj.push(24)
obj.push(56)
obj.display()
param_2 = obj.peek()
obj.display()
param_3 = obj.pop()
param_4 = obj.empty()
print(None, None, None, param_2, param_3, param_4)

