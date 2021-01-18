def staircase(data):

    current = 0

    if data > 0 and data <= 20:
        while current <= data: # While the 'current' counter variable is less or equal to the input value 'data' the loop will continue to execute
            print('#' * current) # This line will print the hash symbol by the current value of the 'current' counter
            current = current + 1 # This increment will ensure on each line a different number of hash symbols will be printed and will also casue the loop to end when it is equal to 'data'

staircase(10)