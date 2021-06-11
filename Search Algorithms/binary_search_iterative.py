

# Binary search continuously splits the sorted given sequence until it either finds the value, or returns None
# Runs in ##### Time

def binary_search_iterative(tofind, sequence):
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