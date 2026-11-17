class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        station_information = list(zip(gas, cost))
        total_tank = 0
        current_tank = 0
        optimal_index = 0

        for current_index in range(len(station_information)):
            current_gas, current_cost = station_information[current_index]
            difference = current_gas - current_cost
            
            total_tank += difference

            if (current_tank + difference) < 0:
                optimal_index = current_index + 1
                current_tank = 0
            else:
                current_tank += difference
        
    
        return optimal_index
        