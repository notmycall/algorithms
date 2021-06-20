import verify

'''
Bubble Sort:

Bubble sort is a sorting algorithm that takes a sequence and begins by comparing the first two values.
If the value on the right is lower than the value on the left, the values are switched. If not, the values are not switched.
This process then shifts by one value to the right, and then it repeats, comparing values to each other. This continues until
the end is reached in which the algorithm starts again, but this time  the length of the sequence is reduced by one. 
The algorithm stops after either all the values have been placed in the correct positions, or no switches are made.

Below is an optimised version of the algorithm, which does not iterate through sorted valued on the right hand side, 
and can also stop running if no sorts are made through an entire iteration.
'''


def bubble_sort_iterative(a): # Accepts a list/array
    l = len(a) # The length of the sequence
    for i in range(l): # Iterating through the sequence
        sort = False
        for j in range(l-i-1): # Each time this is iterated
            if a[j] > a[j+1]:
                sort = True
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
        if sort == False:
            return a
    return a

def bubble_sort_recursive(a):
    pass



# Verify that the algorithm works
unsorted = verify.get_unsorted_list()
print("Unsorted Sequence:", unsorted)
sorted = bubble_sort_iterative(unsorted)
print("Sorted Sequence:  ", sorted)
print("Sorted?", verify.verify(sorted))


