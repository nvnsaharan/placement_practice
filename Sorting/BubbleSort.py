# We can improve it by using one extra flag. No more
# swaps indicate the completion of sorting.


def sort(A):
    for i in range(len(A)):
        for j in range(i, len(A) - 1):
            print("A")
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    print(A)


sort([2, 1, 5, 3])
