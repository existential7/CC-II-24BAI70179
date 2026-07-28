def bruteforce(arr):
    
    n = len(arr)
    if n < 1:
        return arr
    
    new = []
    for i in range(n):
        p = 1
        for j in range(n):
            if i!=j:
                p *= arr[j]

        new.append(p)
        
        
    return new

l = int(input("Enter length of array: "))
arr = [int(input(f"Enter {i+1} Element : ")) for i in range(l)]

print()
print("---"*7)
print(" "*7,"OutPut")
print()
print(bruteforce(arr))