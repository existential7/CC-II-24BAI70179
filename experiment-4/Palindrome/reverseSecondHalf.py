class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def createLL():
    
    n = int(input("Enter Number of element: "))
    
    if n == 0:
        return None
    
    head = node(int(input("Element :")))
    p = head
    
    for i in range(n - 1):
        Node = node(int(input("Element :")))
        
        p.next = Node
        p = Node
        
    return head

def reverseSecondHalf(head):

    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first = head
    second = prev

    while second:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next

    return True

if __name__ == "__main__":
    print("  "*4, "Palindrome Linked List")
    print("  "*4, "Using reverse second half")

    head = createLL()

    if reverseSecondHalf(head):
        print("Palindrome")
    else:
        print("Not Palindrome")
    