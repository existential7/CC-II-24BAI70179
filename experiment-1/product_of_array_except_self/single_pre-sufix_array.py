def single_pre_suff(arr):
    n = len(arr)
    if n < 2:
        return arr
    
    new = []
    p = 1
    for i in arr:
        new.append(p)
        p *= i
        
    s = 1
    for i in range(len(arr)-1,-1,-1):
        # print(i)
        new[i] *= s
        s *= arr[i]
        
    return new

l = int(input("Enter length of array: "))
arr = [int(input(f"Enter {i+1} Element : ")) for i in range(l)]

print()
print("---"*7)
print(" "*7,"OutPut")
print()
print(single_pre_suff(arr))