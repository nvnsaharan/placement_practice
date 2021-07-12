def merge(A, B):
    C = []
    i, j = 0, 0
    while len(A) + len(B) > i + j:
        if len(A) <= i:
            C.append(B[j])
            j += 1
        elif len(B) <= j:
            C.append(A[i])
            i += 1
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    return C


def divide(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = divide(A[:mid])
        right = divide(A[mid:])
        ans = merge(left, right)
        return ans
    return A


print(divide([2, 1, 5, 3]))
