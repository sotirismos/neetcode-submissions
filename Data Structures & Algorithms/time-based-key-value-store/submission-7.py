class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            left = 0
            right = len(self.store[key]) - 1

            while left <= right:
                mid = (left + right) // 2
                if timestamp < self.store[key][mid][1]:
                    right = mid - 1
                elif timestamp > self.store[key][mid][1]:
                    left = mid + 1
                else:
                    return self.store[key][mid][0]
            return self.store[key][right][0] if right >= 0 else ""
        else:
            return ""

