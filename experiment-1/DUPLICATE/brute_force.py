def bruteforce(arr, k):
    
    if arr is None and k == 0:
        return False
    
    l = len(arr)
    if k > l:
        k = l
    
    for i in range(k):
        org = arr[i]
        
        for j in range(i+1, k):
            if org == arr[j]:
                return True
            
    return False


if __name__ == "__main__":
    lg = int(input("Enter Length: "))
    #arr = [i for j in range(lg): i = int(input("Enter No:"))]
    arr = []
    for i in range(lg):
        arr.append(int(input("Enter No:")))
    
    k = int(input("Enter K : "))
    
    if bruteforce(arr, k):
        print("Dublicate is present ")
        
    else :
        print("No Doublicate Present ")