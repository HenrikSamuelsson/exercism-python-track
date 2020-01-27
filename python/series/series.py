def slices(series, length):
    the_slices = []
    for i in range(len(series) - length + 1):
        the_slices.append(series[i:i + length])
    print(the_slices)
    return the_slices

