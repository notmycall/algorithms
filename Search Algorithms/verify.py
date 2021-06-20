def verify(value, algorithm, sequence):
    index = algorithm(value, sequence)
    if index == None:
        print(f"{value} is not in the sequence.")
    elif sequence[index] == value:
        print(f"{value} is at the index ({index}). {sequence[index]} == {value}")
    else:
        print(f"{value} does not appear to be at the index of ({index}): {sequence[index]} != {value}")
