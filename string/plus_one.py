from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        curr = 0

        while idx >= 0:
            if idx == len(digits) - 1:
                digits[idx] = digits[idx] + 1
                if digits[idx] > 9:
                    digits[idx] = digits[idx] % 10
                    curr += 1

            if idx != len(digits) - 1 and curr != 0:
                digits[idx] = digits[idx] + curr
                if digits[idx] > 9:
                    digits[idx] = digits[idx] % 10
                else:
                    curr -= 1

            idx -= 1

        if curr > 0:
            digits = [1] + digits

        return digits


if __name__ == "__main__":
    l1 = [4, 9, 9, 9]
    s = Solution()

    print(s.plusOne(l1))
