class Solution:
    def pivotIndex(self, nums):

        leftSum = 0
        rightSum = sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx
            leftSum += ele
        return -1


if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]

    s = Solution()
    print(s.pivotIndex(nums))
