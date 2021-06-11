lst = [1, 5, 9 , 25, 34, 36, 53, 63, 64, 89, 100]


def binary_search_recursive(tofind, sequence, begin_index=0, end_index=None):
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




    
print(binary_search_recursive(1, lst))

'''
Accepts a sequence and a value to find. 
'''