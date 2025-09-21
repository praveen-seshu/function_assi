# linear search
arr = [10, 20, 30, 40, 50]
key = 30
for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        break
# Time Complexity: O(n) (worst case: element is at the end or not present)
# Space Complexity: O(1) (no extra space used except variables)


# binary search
arr = [10, 20, 30, 40, 50, 60, 70]
low, high = 0, len(arr)-1
key = 50

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index:", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
# Time Complexity: O(log n)
# Space Complexity: O(1)

# bubble sort
arr = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted:", arr)
# Time Complexity: O(n²) (worst case)
# Space Complexity: O(1)

# max element in the list
arr = [5, 2, 9, 1, 7, 6]
max_val = arr[0]
for i in arr:
    if i > max_val:
        max_val = i
print("Max element:", max_val)
# Time Complexity: O(n)
# Space Complexity: O(1)

#fibonacci series
n=20
i=0
a,b=0,1
while i <= 20:
    i+=1
    print(a,end=" ")
    c=a+b
    a=b
    b=c
#time=O(n)
#space=o(1)





