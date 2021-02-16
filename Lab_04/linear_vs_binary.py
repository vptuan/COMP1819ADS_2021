import time


def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2
        # mid = left + (right - left) // 2 == (left + right) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code

# Create the list 
t0 = time.time()

n = 5000000 # input size
arr = list() # data list
rep = 1000 # how many for running search, balance input creating vs algo running

for i in range(0, n):
    arr.append(i)

print("The time taken for creating a list", time.time() - t0, "seconds")

x = 100000 # searching value

# Linear search 
t1 = time.time()
for r in range(rep):
    result_linear = search(arr, n, x)
t2 = time.time()
if result_linear == -1:
    print("Element is found")

else:
    print("Element is found at index", result_linear)
    
print("The time taken by the linear search function is ", t2 - t1, "seconds")

# Binary search
t3 = time.time()

for r in range(rep):
    result_binary = binarySearch(arr, 0, len(arr) - 1, x)

t4 = time.time()

if result_binary != -1:
    print("Element is found at index" + str(result_binary))

else:
    print("Element is not found")

print("The time taken by the binary search function is ", t4 - t3, "seconds")