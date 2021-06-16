'''
Binary Search Explaination:

Binary search is a an efficent algorithm that locates a specified target value by splitting 
the array in half and disregarding the half that does not contain the desired value and repeating 
this process until the target value is either found or there are no values left to search.
'''


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

def binary_search_recursive(tofind, sequence, begin_index=0, end_index=None): # Runtime of O(log n)
    if end_index == None:
        end_index = len(sequence) -1
    if begin_index > end_index:
        return False
    midpoint = (begin_index + end_index) // 2
    if sequence[midpoint] == tofind :
        return midpoint
    elif sequence[midpoint] < tofind:
        return binary_search_recursive(tofind, sequence, midpoint + 1, end_index)
    else:
        return binary_search_recursive(tofind, sequence, begin_index, midpoint - 1)







lst = [1, 5, 9 , 25, 34, 36, 53, 63, 64, 89, 100]

print(binary_search_iterative(54, lst))








'''
binary search accepts a value to find, and a sequence

begin_index = 0 #the start of the Sequence
end_index = len(sequence) # The end of the sequence

while begin_index is less or equal to end_index
midpoint = calculated from begin and end indexes
if sequence[midpoint] is equal to tofind:
    return midpoint
elif sequence[midpoint] < tofind:
    begin_index = midpoint + 1
elif sequence[midpoint] > tofind:
    end_index = midpoint - 1
  
 


end while
return None

'''