from typing import List


class Solution:
    def longestRun(self, list: List[int]) -> int:

        if not list:
            return []

        def find_max(list: List[int]) -> List[int]:

            longest_run = []
            current_run = [list[0]]

            for i in range(1, len(list)):
                if list[i] >= list[i - 1]:
                    current_run.append(list[i])
                else:
                    if len(current_run) > len(longest_run):
                        longest_run = current_run
                    current_run = [list[i]]

            if len(current_run) > len(longest_run):
                longest_run = current_run

            return longest_run

        def find_min(list: List[int]) -> List[int]:
            if not list:
                return []

            longest_run = []
            current_run = [list[0]]

            for i in range(1, len(list)):
                if list[i] <= list[i - 1]:
                    current_run.append(list[i])
                else:
                    if len(current_run) > len(longest_run):
                        longest_run = current_run
                    current_run = [list[i]]

            if len(current_run) > len(longest_run):
                longest_run = current_run

            return longest_run

        mono_max = find_max(list)
        mono_min = find_min(list)

        if len(mono_max) > len(mono_min):
            return sum(mono_max)
        elif len(mono_max) < len(mono_min):
            return sum(mono_min)
        elif len(mono_max) == len(mono_min):
            first_mono_index = list.index(mono_max[0])
            sec_mono_index = list.index(mono_min[0])

            if first_mono_index > sec_mono_index:
                return sum(mono_min)
            elif first_mono_index < sec_mono_index:
                return sum(mono_max)


if __name__ == "__main__":
    l1 = [3, 2, 4]
    s = Solution()

    print(s.longestRun(l1))
