'''
Quick Sort Explaination: 

Quick sort takes a sequence. If the sequence has the length of 1 or 0, then it is returned
if it isn't, then a pivot is taken from the very end, and the remaining values are split into left and right arrays. These are then fed into quick sort. 
At the end, the left, middle, and right values are merged together and returned
'''

def quick_sort_recursive(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence[length - 1]
    items_lower = []
    items_greater = []
    for i in range(0, length - 1):
        if sequence[i] <= pivot:
            items_lower.append(sequence[i])
        else:
            items_greater.append(sequence[i])
    return quick_sort_recursive(items_lower) + [pivot] + quick_sort_recursive(items_greater)






