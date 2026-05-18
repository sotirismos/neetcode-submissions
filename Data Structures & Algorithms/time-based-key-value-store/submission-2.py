class TimeMap:

    def __init__(self):
        self.store: dict[dict[int, str]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            else:
                for time in range(timestamp, -1 , -1):
                    if time in self.store[key]:
                        return self.store[key][time]
                return ""


