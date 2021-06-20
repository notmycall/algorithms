import math
'''
Jump Search:

Works similar to sequential search but takes jumps instead. 
Accepts a sequence and target value. 
Begins at the first index. If the value is equal to the target value, the program returns.
Otherwise the program jumps to the next index and compares the value. If the value is equal, it returns the index position, 
but if it isn't then it compares the value to the target. If the value is lower than the target, it continues, otherwise it 
begins counting down backwards an m number of times comparing the value on each iteration. If the value is not found, then the program returns None.

Has a runtime of O(sqr(n))
'''

def jump_search_iteritive(tofind, a):
    n = len(a) # Length of the Array
    step = int(math.sqrt(len(a))) # The size of the jump
    prev = 0


    while a[min(step, n)-1] < tofind: # Finds the block where the number could be in
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None

    while a[prev] < tofind: # Iterates through the numbers until either
        prev += 1
        if prev == min(step, n):
            return None

    if a[prev] == tofind:
        return prev

    return None


a = [1, 3, 5, 9, 10, 12, 15, 18, 22, 26, 27, 39]
print(jump_search_iteritive(18, a))