import random

def verify(sequence): # Verifies that the sequence is in order
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True

def get_unsorted_list(): # Gets a unsorted list. Will run until an unsorted list is verified to be unsorted and returned.
    unsorted = []
    for i in range(20):
        unsorted.append(random.randint(0, 100))
    if verify(unsorted):
        return get_unsorted_list()
    else:
        return unsorted