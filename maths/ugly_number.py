class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1


if __name__ == "__main__":
    n = 6

    s = Solution()
    print(s.isUgly(n))
