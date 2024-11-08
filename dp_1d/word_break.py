from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}  # Dictionary to store results of subproblems

        def dfs(i):
            # If we've reached the end of the string, return True
            if i == len(s):
                return True

            # If the result for this index is already computed, return it
            if i in memo:
                return memo[i]

            # Try every possible end position for the current substring
            for j in range(i, len(s)):
                if s[i: j + 1] in wordSet:
                    if dfs(j + 1):
                        memo[i] = True  # Cache the result before returning
                        return True

            # If no valid word break found, cache the result as False
            memo[i] = False
            return False

        return dfs(0)
