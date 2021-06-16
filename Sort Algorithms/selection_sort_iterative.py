import verify

'''
Selection Sort Explaination: 


'''


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



# Verify that the algorithm works
unsorted = verify.get_unsorted_list()
print("Unsorted Sequence:", unsorted)
sorted = selection_sort_itertive(unsorted)
print("Sorted Sequence:", sorted, )
print("Sorted?", verify.verify(sorted))