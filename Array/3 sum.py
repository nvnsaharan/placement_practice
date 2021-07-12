# def solve(A, pos, cur):
#     if len(cur) == 3:
#         if sum(cur) == 0:
#             print(cur)
#         return
#     for i in range(pos, len(A)):
#         cur.append(A[i])
#         solve(A, i + 1, cur)
#         cur.pop()
# A = list(map(int, input().split()))
# solve(A, 0, [])


def solve(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append(a, nums[l], nums[r])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
