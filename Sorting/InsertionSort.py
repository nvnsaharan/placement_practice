def sort(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]

    print(A)


sort([2, 1, 5, 3])
