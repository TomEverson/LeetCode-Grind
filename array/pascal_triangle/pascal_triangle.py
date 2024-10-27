from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(1, numRows + 1):
            list = [0] * i
            list[0], list[-1] = 1, 1

            if i < 3:
                res.append(list)
                continue

            for j in range(1, len(list) - 1):
                sub_list = res[-1]
                list[j] = sub_list[j] + sub_list[j-1]
            res.append(list)

        return res


if __name__ == "__main__":
    s = Solution()

    print(s.generate(5))
