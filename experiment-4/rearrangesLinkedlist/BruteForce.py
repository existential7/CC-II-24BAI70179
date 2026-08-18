import os, sys

base = os.path.dirname(__file__)
pro = os.path.abspath(os.path.join(base, r"..\.."))
sys.path.append(pro)

from slowtype import slowtype
 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def createLL():
    
    n = int(input("Enter length: "))
    if n < 1: 
        return None
    
    
    head = Node(int(input("Element: ")))
    surf = head
    for i in range(n - 1):
        surf.next = Node(int(input("Element: ")))
        surf = surf.next
        
    return head

def bruteForce(head):
    
    lis = []
    new = head
    
    while(head != None):
        lis.append(head.data)
        head = head.next
      
    head = new  
    for i in range(0, len(lis), 2):
        head.data = lis[i]
        head = head.next
        
    for i in range(1, len(lis), 2):
        head.data = lis[i]
        head = head.next
        
    return new

def display(head):
    
    print("\n Output: \n   ",end = '')
    while head:
        print(f"->{head.data}", end = " ")
        head = head.next
        
    print("\n")
        


if __name__ == "__main__":
    
    slowtype("         Position rearranges ")
    slowtype("             Using Brute Force Attempt\n\n")
    
    
    head = createLL()
    head = bruteForce(head)
    
    display(head)