def slidewin(arr, k):
    l = len(arr)
    if l < 2 or k == 0:
        return False
    
    k+=1
    if k > l:
        k = l
        
    test = arr[1:k]
    # print(test)
    
    for i in range(l-1):
        # print(test,"   ", arr[i])
        
        for p in test:
            if p == arr[i]:
                return True 
            
        test.pop(0)
        last = i+k
        if last > l:
            last = l
        test.append(arr[last-1])
        
    
    return False

if __name__ == "__main__":
    lg = int(input("Enter Length: "))
    arr = [int(input(f"{i+1} Element: ")) for i in range(lg)]
    k = int(input("Enter K : "))
    
    if slidewin(arr, k):
        print("Duplicate Found ")
    else:
        print("No Duplicate Found ")
        
    # print(slidewin([1,2,3,4,1], 3))