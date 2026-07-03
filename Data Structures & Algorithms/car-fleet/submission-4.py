class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_stack = []
        cars = zip(speed, position)
        cars_pos_sorted = sorted(cars, key=lambda x: x[1])
        for speed, position in cars_pos_sorted:
            time = (target - position) / speed
            while fleet_stack:
                if time >= fleet_stack[-1]:
                    fleet_stack.pop()
                else:
                    break
            fleet_stack.append(time)
        return len(fleet_stack)
