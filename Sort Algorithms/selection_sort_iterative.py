def selection_sort_itertive(sequence):
    for i in range(len(sequence)):
        target_index  = i
        smallest_index = i
        for x in range(i, len(sequence)):
            if sequence[smallest_index] > sequence[x]:
                smallest_index = x
        # Replace current value with smallest
        temp = sequence[target_index]
        sequence[target_index] = sequence[smallest_index]
        sequence[smallest_index] = temp
    return sequence


def verify(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True

sequence = [22, 27, 54, 87, 91, 71, 82, 98, 68, 95, 22, 85, 29, 83, 77, 72, 25, 29, 
68, 32, 69, 24, 56, 92, 43, 20, 81, 75, 69, 96, 34, 
42, 8, 34, 83, 29, 34, 33, 65, 92, 67, 45, 56, 29, 34, 
86, 4, 1, 29, 81, 52, 74, 2, 1, 95, 80, 40, 65, 73, 79, 
57, 84, 39, 51, 65, 80, 30, 41, 99, 80, 10, 59, 29, 22, 
11, 72, 1, 23, 63, 82, 24, 81, 30, 80, 40, 33, 94, 35, 
43, 89, 76, 40, 100, 6, 4, 57, 62, 22, 68, 94]      


print(verify(sequence)) # Should return False if unsorted
print(sequence)

sorted_sequence = selection_sort_itertive(sequence) # Store a stored sequence
print(verify(sorted_sequence)) # Should return True as it has been sorted
print(sorted_sequence)