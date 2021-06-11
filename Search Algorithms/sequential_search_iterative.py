lst = [1, 5, 9 , 25, 34, 36, 53, 63, 64, 89, 100]

# Sequential search iterates through the sequence to find a given value. 
# It takes O(n) time to run. 

def sequential_search_iterative(tofind, sequence):
    for index in range(len(sequence)):
        if sequence[index] == tofind:
            return index
    return None
        
print(sequential_search_iterative(101, lst))