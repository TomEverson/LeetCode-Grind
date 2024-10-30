import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = [n for n in range(1, 1001)]
        self.hashset = set(self.min_heap)
        heapq.heapify(self.min_heap)

    def popSmallest(self) -> int:
        num = heapq.heappop(self.min_heap)
        self.hashset.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num in self.hashset:
            return None
        self.hashset.add(num)
        heapq.heappush(self.min_heap, num)


# # if __name__ == "__main__":
# #     smallestInfiniteSet = SmallestInfiniteSet()
# #     smallestInfiniteSet.addBack(2)
# #     smallestInfiniteSet.popSmallest()
# #     smallestInfiniteSet.popSmallest()
# #     smallestInfiniteSet.popSmallest()
# #     smallestInfiniteSet.addBack(1)
# #     smallestInfiniteSet.popSmallest()
# #     smallestInfiniteSet.popSmallest()
# #     smallestInfiniteSet.popSmallest()

list = [1, 2, 3, 1]

num = heapq.heappop(list)

print(num, list)
