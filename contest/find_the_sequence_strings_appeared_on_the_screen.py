from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:

        res = []
        temp_str = ''

        for index, letter in enumerate(target):
            start_letter = "a"

            res.append(temp_str + start_letter)

            while letter != start_letter:
                start_letter = chr(ord(start_letter) + 1)
                res.append(temp_str + start_letter)
            temp_str += start_letter

        return res


if __name__ == "__main__":
    target = "abc"

    solution = Solution()

    print(solution.stringSequence(target))
