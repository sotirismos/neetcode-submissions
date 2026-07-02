class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_value:
            if self.min_value[-1] > val:
                self.min_value.append(val)
            else:
                self.min_value.append(self.min_value[-1])
        else:
            self.min_value.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]
