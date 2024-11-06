from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []

        self.subset = []
        self.dfs(0)
        return self.res

    def dfs(self, i: int):
        if i == len(self.nums):
            self.res.append(self.subset.copy())
            return

        self.subset.append(self.nums[i])
        self.dfs(i + 1)

        # decision NOT to include nums[i]
        self.subset.pop()
        self.dfs(i + 1)


if __name__ == "__main__":
    l1 = [1, 2, 3]

    s = Solution()
    print(s.subsets(l1))
