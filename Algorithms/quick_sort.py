def quicksort(x):
    if len(x) < 2:
        return x
    pivot = x[0]
    less = [i for i in x[1:] if i <= pivot]
    greater = [i for i in x[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
