import verify # Used for verifying that the algorithm is working as intended

'''
Quick Sort: 

Quick sort accepts a sequence. If the sequence has the length of 1 or 0, then it is returned.
if it doesn't, then a pivot is taken from the very end, and the remaining values are split into left and right sequences. 
The sequences are then sorted recursively until all the sequences are sorted and returned as one.

Has a runtime of O(n log n)
'''
# Algorithm
def quick_sort_recursive(sequence):
    length = len(sequence)
    if length <= 1: # Returns the sequence if the length is 0 or 1. This is the base case.  
        return sequence
    else:
        pivot = sequence[length - 1] # Uses the end value as the pivot
    items_lower = [] 
    items_greater = []
    for i in range(0, length - 1):
        if sequence[i] <= pivot: 
            items_lower.append(sequence[i]) # Stored in items_lower if the value is less than pivot
        else:
            items_greater.append(sequence[i]) # Stored in items_greater if the value is greater than pivot

    # Uses recursion to sort the values. Merges the lower, pivot, and greater values into one sequence.
    return quick_sort_recursive(items_lower) + [pivot] + quick_sort_recursive(items_greater) 


# Verify that the algorithm works
unsorted = verify.get_unsorted_list()
print("Unsorted Sequence:", unsorted)
sorted = quick_sort_recursive(unsorted)
print("Sorted Sequence:  ", sorted)
print("Sorted?", verify.verify(sorted))


