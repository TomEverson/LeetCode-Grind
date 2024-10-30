from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        hashSet = set()

        for n in arr:
            hashmap[n] = hashmap.get(n, 0) + 1

        for n in hashmap.values():
            if n in hashSet:
                return False
            hashSet.add(n)

        return True


if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    s = Solution()

    print(s.uniqueOccurrences(arr))
