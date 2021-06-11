lst = [1, 5, 9 , 25, 34, 36, 53, 63, 64, 89, 100]

def sequential_search_recursive(tofind, sequence, current_index = 0): # Accepts the value to find, the sequence/array/list, and an optional current index parametre
    if current_index > len(sequence) - 1:
        return
    if tofind == sequence[current_index]:
        return current_index
    else:
        return sequential_search_recursive(tofind, sequence, current_index+1)
print(sequential_search_recursive(101, lst))