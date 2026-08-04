def insertInto(arr, tar):
    
    n = len(arr)
    if n == 0 or tar < arr[0]:
        return 0
    
    
    for i in range(n):
        if tar <= arr[i]:
            if tar == arr[i]:
                print(" Target Element is already present at ",i)
            return i
    
    return n

if __name__ == "__main__":
    print(" "*10," Brute Force\n")
    n = int(input(" Enter length of array: "))
    
    print()
    arr = [int(input(f" Element {i} : ")) for i in range(n)]
    
    tar = int(input(" Enter Target Value: "))
    print()
    
    print(f"     >>>  Output: {insertInto(arr,tar)}")
    print("\n -----------------------------------------------------\n")