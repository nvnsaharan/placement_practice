def sort(A):
    for i in range(len(A)):
        cur = A[i]
        j = i
        while j and cur < A[j - 1]:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur

    print(A)


sort([2, 1, 5, 3])
