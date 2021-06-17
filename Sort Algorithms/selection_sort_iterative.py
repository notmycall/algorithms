import verify # Used for verifying that the algorithm is working as intended

'''
Selection Sort: 

Selection sort takes an array and sorts a single element during each iteration. 
It sets the left most unsorted value as the smallest value and iterates through the values. 
If a value is the equal or greater to the smallest value, it continues to the next value, but if the value is smaller
then it sets the current value as the smallest index. After the final value is reached, the values at the target 
index and smallest indexs are flipped. This is performed until all the values are sorted. 

Has a run time of O(n^2)
'''
# Algorithm
def selection_sort_itertive(sequence): # Accepts a sequence. Doesn't check if the sequence is sorted or not. 
    for i in range(len(sequence)): 
        target_index  = i # The index of the value being compared to the other values in the array
        smallest_index = i # The index of the smallest value within the sequence. It is initially the same as the target index. 
        for x in range(i, len(sequence)): # Iterates through the values to the right of the target index
            if sequence[smallest_index] > sequence[x]: # Executes if a smaller value is found
                smallest_index = x # Replaces the smallest index with the index of the current value
                
        # Swaps the values at the target and smallest indexes with the help of a temporary variable. 
        temp = sequence[target_index] 
        sequence[target_index] = sequence[smallest_index]
        sequence[smallest_index] = temp
    return sequence



# Verify that the algorithm works
unsorted = verify.get_unsorted_list()
print("Unsorted Sequence:", unsorted)
sorted = selection_sort_itertive(unsorted)
print("Sorted Sequence:  ", sorted)
print("Sorted?", verify.verify(sorted))