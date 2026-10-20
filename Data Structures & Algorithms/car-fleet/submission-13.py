class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(speed, position)
        cars_pos_sorted = sorted(cars, key=lambda x: x[1])
        stack = []

        for speed, position in cars_pos_sorted:
            time_at_destination = (target - position) / speed

            while stack and time_at_destination >= stack[-1]:
                stack.pop()
            stack.append(time_at_destination)  

        return len(stack)   
