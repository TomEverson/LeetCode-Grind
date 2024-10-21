class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for idx, num in enumerate(nums):
            if idx == 0:
                hashmap[num] = idx
            else:
                sub_num = target - num
                if sub_num in hashmap:
                    return [hashmap[sub_num], idx]
                else:
                    hashmap[num] = idx


solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
