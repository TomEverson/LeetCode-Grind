from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []

        def dfs(i, total):
            if total == target:
                res.append(current.copy())
                return
            if i >= len(nums) or total > target:
                return

            current.append(nums[i])
            dfs(i, total + nums[i])
            current.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    s = Solution()
    print(s.combinationSum(candidates, target))
