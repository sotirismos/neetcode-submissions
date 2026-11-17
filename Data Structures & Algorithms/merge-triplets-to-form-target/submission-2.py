class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        is_x = False
        is_y = False
        is_z = False

        for triplet in triplets:
            diff_x = triplet[0] - target[0]
            diff_y = triplet[1] - target[1]
            diff_z = triplet[2] - target[2]

            if diff_x > 0 or diff_y > 0 or diff_z > 0:
                continue
            else:
                if diff_x == 0:
                    is_x = True
                if diff_y == 0:
                    is_y = True
                if diff_z == 0:
                    is_z = True
        
        return is_x and is_y and is_z
