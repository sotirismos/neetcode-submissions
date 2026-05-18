class TimeMap:

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res

        entries = self.store[key]  

        left = 0
        right = len(entries) - 1
        while left <= right:
            mid = (left + right) // 2
            if entries[mid][1] <= timestamp:
                res = entries[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

