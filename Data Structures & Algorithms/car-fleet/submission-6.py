class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(speed, position)
        cars_sorted = sorted(cars, key=lambda x: x[1])

        fleet_stack = []
        for speed, position in cars_sorted:
            time_to_destination = (target - position) / speed
            if not fleet_stack:
                fleet_stack.append(time_to_destination)
            else:
                if time_to_destination < fleet_stack[-1]:
                    fleet_stack.append(time_to_destination)
                else:
                    while fleet_stack and time_to_destination >= fleet_stack[-1]:
                        fleet_stack.pop()
                    fleet_stack.append(time_to_destination)
        
        return len(fleet_stack)
