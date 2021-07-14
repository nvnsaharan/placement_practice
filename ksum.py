# still not working


def ksum(nums, target, k, begin):
    if begin >= len(nums):
        return []  # base case
    elif k == 2:
        # code 2sum problem
        res = []
        i = begin
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return res
    else:
        res = []
        for i in range(begin, len(nums) - k + 1):
            if (
                i > begin
                and nums[i] == nums[i - 1]
                or nums[i] + nums[-1] * (k - 1) < target
            ):
                continue
            # the first condition is to remove Duplicates
            # the second Condition is that if we consider element nums[i]
            # whether we get required target or not
            # ie if we consider nums[i] which is smallest in current
            # ksum size windown and ksum-1 times of largest number in
            # the nums and still we get sum < target the we do not need
            # to consider nums[i]
            if nums[i] + nums[i + 1] * (k - 1) > target:
                break

            r = ksum(nums, target - nums[i], k - 1, i + 1)

            for elm in r:
                elm.insert(0, nums[i])
            # We insert current nums[i] to the result of ksum-1 result

            for elm in r:
                res.append(elm)
            print(res)
        return res


nums = [1, 0, -1, 0, -2, 2]
print(ksum(nums, 0, 4, 0))
