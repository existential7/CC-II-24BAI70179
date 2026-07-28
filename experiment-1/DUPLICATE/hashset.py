def hashset(arr, k):
    if arr is None and k == 0:
        return False
    
    l = len(arr)
    if k > l:
        k = l
        
    for i in range(len(arr)-k):
        el = arr[i]
        
        for j in arr[i+1:i+k+1]:
            if el == j:
                return True
            
    return False
    


if __name__ == "__main__":
    lg = int(input("Enter Length: "))
    arr = [int(input(f"{j+1} Element: ")) for j in range(lg)]
    
    k = int(input("Enter K : "))
    
    if hashset(arr, k):
        print("Duplicate is present ")
        
    else :
        print("No Duplicate Present ")