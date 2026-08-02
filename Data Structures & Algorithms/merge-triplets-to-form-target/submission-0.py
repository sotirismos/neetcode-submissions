class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        is_value_present = [False, False, False]

        for triplet in triplets:
            diff_x = target[0] - triplet[0]
            diff_y = target[1] - triplet[1]
            diff_z = target[2] - triplet[2]

            if diff_x < 0 or diff_y < 0 or diff_z < 0:
                continue
            else:
                if diff_x == 0:
                    is_value_present[0] = True
                if diff_y == 0:
                    is_value_present[1] = True
                if diff_z == 0:
                    is_value_present[2] = True              

        for value in is_value_present:
            if not value:
                return False
        
        return True
