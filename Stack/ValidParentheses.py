def solve(s):
    a = []
    for i in s:
        if i == ")":
            if a.pop() == "(":
                continue
            else:
                return False
        elif i == "}":
            if a.pop() == "{":
                continue
            else:
                return False
        elif i == "]":
            if a.pop() == "[":
                continue
            else:
                return False
        else:
            a.append(i)
    if len(a):
        return False
    return True


print(solve("()"))
print(solve("([)]"))
print(solve("()[]{}"))
