def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    d = dict()
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] >= k:
            print(i, end=" ")


solve()
