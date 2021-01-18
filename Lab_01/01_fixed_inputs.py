def minmax(sequence):
    min = max = sequence[0] # assuming nonempty
    for val in sequence:
        if val < min:
            min = val
        if val > max:
            max = val
    return min, max

print(minmax([1,2,3,5]))
print(minmax([0,1,-2]))
print(minmax([3]))