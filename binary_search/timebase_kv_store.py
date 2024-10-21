class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        if not self.hashmap[key]:
            return res

        #! [[1, "bar"], [3, "bar2"]]
        values = self.hashmap[key]

        if len(values) == 1:
            return values[0][1]

        left_ptr, right_ptr = 0, len(values) - 1

        while left_ptr <= right_ptr:
            midpoint = (left_ptr + right_ptr) // 2
            if values[midpoint][0] <= timestamp:
                res = values[midpoint][1]
                left_ptr = midpoint + 1
            else:
                right_ptr = midpoint - 1
        return res


timeMap = TimeMap()
# store the key "foo" and value "bar" along with timestamp = 1.
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)         # return "bar"


# # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.get("foo", 3)
# # store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)         # return "bar2"
timeMap.get("foo", 5)         # return "bar2"

print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
