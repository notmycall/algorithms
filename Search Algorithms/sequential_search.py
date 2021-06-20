'''
Sequential Search Explaination: 

# Sequential search iterates through the sequence to find a given value.
If the current value is the same as the target value, the index is returned. 
Otherwise, it moves on to the next value. 
If no values are found to match, None is returned.

Has a runtime of O(n)
'''


def sequential_search_iterative(tofind, sequence):
    for index in range(len(sequence)):
        if sequence[index] == tofind:
            return index
    return None


def sequential_search_recursive(tofind, sequence, current_index = 0):
    if current_index > len(sequence) - 1:
        return
    if tofind == sequence[current_index]:
        return current_index
    else:
        return sequential_search_recursive(tofind, sequence, current_index+1)