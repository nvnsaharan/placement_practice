def calculateSpan(a, n):
    span = [0 for i in range(n)]
    span[0] = 1
    s = [0]
    for i in range(1, n):
        while len(s) and a[s[-1]] <= a[i]:
            s.pop()
        if len(s) == 0:
            span[i] = i + 1
        else:
            span[i] = i - s[-1]

        s.append(i)
    return span
