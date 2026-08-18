class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLL():
    n = int(input("Enter Number of Elements: "))

    if n == 0:
        return None

    head = Node(int(input("Enter element: ")))
    p = head

    for i in range(n - 1):
        node = Node(int(input("Enter element: ")))
        p.next = node
        p = node

    return head


def bruteForce(head):
    arr = []

    while head is not None:
        arr.append(head.data)
        head = head.next

    return arr == arr[::-1]


if __name__ == "__main__":
    print(" "*4, "Palindrome Linked List")
    print(" "*4, "Using Brute Force")

    head = createLL()

    if bruteForce(head):
        print("Palindrome")
    else:
        print("Not Palindrome")
    
    