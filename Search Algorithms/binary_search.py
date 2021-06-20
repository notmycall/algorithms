import verify

'''
Binary Search:

Binary search accepts a sorted sequence and the value to find. The sequence is split in half and the middle value is compared to the value to find.
If the middle value is equal to the value to find, then the middle index is returned. 
If not, the sequence that cannot contain the value is disposed and the steps are repeated on the left over half. 
This continues until the value is found or the start index is greater than the end index.


Has a runtime of O(log n)
'''

# Iterative Implementation
def binary_search_iterative(tofind, sequence): # Runtime of O(log n)
    begin_index = 0
    end_index = len(sequence) - 1
    while begin_index <= end_index:
        #midpoint = begin_index + (end_index - begin_index) // 2
        midpoint = (begin_index + end_index) //2
        if sequence[midpoint] == tofind: # If the midpoint of the sequence is the value, return it
            return midpoint
        elif sequence[midpoint] < tofind: # If midpoint less than tofind, delete left half
            begin_index = midpoint + 1
        else:
            end_index = midpoint - 1
    return None

# Recursive Implementation
def binary_search_recursive(tofind, sequence, begin_index=0, end_index=None): # Runtime of O(log n)
    if end_index == None:
        end_index = len(sequence) -1
    if begin_index > end_index:
        return None
    midpoint = (begin_index + end_index) // 2
    if sequence[midpoint] == tofind :
        return midpoint
    elif sequence[midpoint] < tofind:
        return binary_search_recursive(tofind, sequence, midpoint + 1, end_index)
    else:
        return binary_search_recursive(tofind, sequence, begin_index, midpoint - 1)


sorted_sequence = [2, 8, 9, 10, 12, 24, 35, 38, 44, 46, 48, 59, 59, 64, 66, 67, 82, 91, 96, 99]
verify.verify(12, binary_search_iterative, sorted_sequence)
verify.verify(37, binary_search_iterative, sorted_sequence)
verify.verify(2, binary_search_iterative, sorted_sequence)
verify.verify(99, binary_search_iterative, sorted_sequence)
print()
verify.verify(12, binary_search_recursive, sorted_sequence)
verify.verify(37, binary_search_recursive, sorted_sequence)
verify.verify(2, binary_search_recursive, sorted_sequence)
verify.verify(99, binary_search_recursive, sorted_sequence)