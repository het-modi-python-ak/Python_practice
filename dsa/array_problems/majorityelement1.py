# Given an array arr[] of size n, find the element that appears more than ⌊n/2⌋ times. If no such element exists, return -1.

# Examples:

# Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
# Output: 1
# Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.

# Input: arr[] = [7]
# Output: 7
# Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.

# Input: arr[] = [2, 13]
# Output: -1
# Explanation: No element appears more than ⌊2/2⌋ = 1 time, so there is no majority element.


def fun1(arr):
    sorted(arr)
    n= len(arr)
    ct=1
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            ct+=1

        if ct>=n/2:
            return arr[i]

    return -1; 


print(fun1([2,2,1]))



#second way
def fun2(arr):

    n = len(arr)
    candidate = -1
    count = 0

    # Find maximum key
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

   
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    
    if count > n // 2:
        return candidate
    else:
        return -1

if __name__ == "__main__":
    
    arr = [1, 1, 2, 1, 3, 5, 1]
    print(fun2(arr))
