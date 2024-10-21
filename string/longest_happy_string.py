class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letter_map = {
            "a": a,
            "b": b,
            "c": c,
        }

        max_letter = max(letter_map, key=letter_map.get)
        temp = 0
        res = ""

        while max(letter_map.values()) >= 2:

            if temp == 2:
                min_letter = min(
                    (key for key in letter_map if letter_map[key] > 0), key=letter_map.get)
                print("min", min_letter, letter_map)

                if res[-1] == min_letter:
                    break
                res += min_letter
                letter_map[min_letter] -= 1
                temp = 0

            else:
                res += max_letter
                letter_map[max_letter] -= 1
                max_letter = max(letter_map, key=letter_map.get)
                temp += 1

        return res


solution = Solution()

print(solution.longestDiverseString(1, 1, 7))  # ! "ccaccbcc"
