def lowerBondApproach(arr, tar):
    
    n = len(arr)
    if n == 0 or tar < arr[0]:
        return 0
    
    start, end = 0, n-1
    mid = end//2
    
    while (start < end):
        
        if tar < arr[mid]:
            end = mid
        else:
            start = mid+1
            
        mid = (start + end)//2
    
    if tar == arr[mid]:
        print(" Target Element is already present at ",mid -1)
        return mid-1
        
    return mid

if __name__ == "__main__":
    print(" "*10," Brute Force\n")
    n = int(input(" Enter length of array: "))
    
    print()
    arr = [int(input(f" Element {i + 1} : ")) for i in range(n)]
    
    tar = int(input(" Enter Target Value: "))
    print()
    
    print(f"     >>>  Output: {lowerBondApproach(arr,tar)}")
    print("\n -----------------------------------------------------\n")
    