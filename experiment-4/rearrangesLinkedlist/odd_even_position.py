import sys, time

def slowtype(data):
    for i in data:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

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


def position(head):
    if head is None:
        return None

    odd = head
    even = head.next
    ph = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = ph

    return head


def display(head):
    
    print("\n Output: \n   ",end = '')
    while head:
        print(f"->{head.data}", end = " ")
        head = head.next
        
    print("\n")
        


if __name__ == "__main__":
    
    print(" "*8)
    slowtype("Position rearranges ")
    print(" "*8)
    slowtype("   Using Optimal solution \n\n")
    
    
    head = createLL()
    head = position(head)
    
    display(head)