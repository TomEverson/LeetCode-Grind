from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i: int):
            if i == len(s):
                res.append(subset.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j + 1)
                    subset.pop()

        dfs(0)
        return res

    def isPalindrome(self, s: str):
        if len(s) == 1:
            return True

        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    s = "aab"
    sol = Solution()

    print(sol.partition(s))
