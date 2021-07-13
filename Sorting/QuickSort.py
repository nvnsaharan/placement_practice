def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop()

    itemsGreat, itemslow = [], []
    for i in A:
        if i > pivot:
            itemsGreat.append(i)
        else:
            itemslow.append(i)
    return quicksort(itemslow) + [pivot] + quicksort(itemsGreat)


A = [2, 1, 5, 3, 3, 4, 1, 8, 13, 19, 5, 6, 0]
print(quicksort(A))
