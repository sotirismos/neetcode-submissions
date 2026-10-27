class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            if timestamp < self.store[key][0][1]:
                return ""
            else:
                left = 0 
                right = len(self.store[key]) - 1
                
                while left <= right:
                    mid = (left + right) // 2

                    if timestamp < self.store[key][mid][1]:
                        right = mid - 1
                    else:
                        left = mid + 1

                return self.store[key][right][0]