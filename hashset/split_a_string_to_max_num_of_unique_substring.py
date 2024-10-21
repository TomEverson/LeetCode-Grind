class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        hashset = set()
        left_ptr = 0
        max_splits = 0

        for right_ptr in range(len(s)):
            substring = s[left_ptr:right_ptr + 1]

            if substring not in hashset:
                hashset.add(substring)
                max_splits += 1
                left_ptr = right_ptr + 1

        return max_splits


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxUniqueSplit("ababccc"))  # ? 5
