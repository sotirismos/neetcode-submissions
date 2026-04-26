class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars_sorted = sorted(cars, key=lambda x: x[0], reverse=True)
        fleet_times = []
        for car in cars_sorted:
            required_time = (target - car[0]) / car[1]
            if len(fleet_times) != 0 and required_time <= fleet_times[-1]:
                continue
            else:
                fleet_times.append(required_time)
        
        return len(fleet_times)
                
