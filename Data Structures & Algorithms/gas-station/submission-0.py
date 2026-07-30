class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Step 1: Find possible starting stations
        possible_station_indices = []
        for index, gas_amount in enumerate(gas):
            if gas_amount >= cost[index]:
                possible_station_indices.append(index)

        # Step 2: For each starting station go clockwise and try to complete the circle
        for index in possible_station_indices:
            gas_left = 0
            current_station = index
            # Step 2.1: Complete the rightmost part
            while current_station < len(gas):
                gas_left += gas[current_station]
                gas_left -= cost[current_station]
                if gas_left < 0:
                    break
                current_station += 1

            if current_station != len(gas):
                continue

            # Step 2.2: Complete the leftmost part
            current_station = 0
            while current_station < index:
                gas_left += gas[current_station]
                gas_left -= cost[current_station]
                if gas_left < 0:
                    break
                current_station += 1
            # If we reach this point we completed the circle

            if current_station != index:
                continue

            return index

        return -1  
