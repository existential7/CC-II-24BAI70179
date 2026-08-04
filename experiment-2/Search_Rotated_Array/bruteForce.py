def bruteForce(arr, tar):
    
    n = len(arr)
    if n < 1:
        print(" Input Array is Empty")
        return -1
    
    for i in range(n):
        if tar == arr[i]:
            return i
        
    print(f"     >>>  Output: Target {tar} not Found in Array ")
    return -1

if __name__ == "__main__":
    print(" "*10," Brute Force\n")
    n = int(input(" Enter length of Array: "))
    
    print()
    arr = [int(input(f" Element {i + 1} : ")) for i in range(n)]
    
    tar = int(input(" Enter Target Value: "))
    print()
    
    op = bruteForce(arr, tar)
    if (op != -1):
        print(f"     >>>  Output: Target {tar} at Index {op}")
    print("\n -----------------------------------------------------\n")