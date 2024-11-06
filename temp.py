from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = 0

        for num in nums:
            if num in hashmap:
                if hashmap[num] == 1:
                    res = res ^ num
            hashmap[num] = hashmap.get(num, 0) + 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.duplicateNumbersXOR([1, 2, 2, 1]))
