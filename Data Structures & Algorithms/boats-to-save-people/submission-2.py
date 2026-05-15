class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0 
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[right] >= limit:
                boats += 1
                right -= 1
                continue
            summed_weight = people[right] + people[left]
            if summed_weight > limit:
                boats += 1
                right -= 1
            else:
                boats += 1
                left += 1
                right -= 1
        return boats
