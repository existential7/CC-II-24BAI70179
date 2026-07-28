def pre_suffix(arr):
    n = len(arr)
    if n < 2:
        return arr
    
    suf = []
    pre = [1]*n
    
    s = 1
    p = 1
    for i in range(n):
        suf.append(s)
        pre[n-i-1] *= p
        p *= arr[n-i-1]
        s *= arr[i]

    for i in range(n):
        suf[i] *= pre[i]

    return suf

l = int(input("Enter length of array: "))
arr = [int(input(f"Enter {i+1} Element : ")) for i in range(l)]

print()
print("---"*7)
print(" "*7,"OutPut")
print()
print(pre_suffix(arr))