def solve():
    n = int(input())
    A = list(map(int, input().split()))
    sm = 0
    for i in A:
        sm = max(i, sm + i)
    print(sm)


solve()
