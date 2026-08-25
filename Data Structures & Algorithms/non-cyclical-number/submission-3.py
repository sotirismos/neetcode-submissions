class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        sum_results = set()

        while True:
            sum_n = 0
            for str_digit in n_str:
                sum_n += int(str_digit) ** 2
            
            # Check if we completed a cycle
            if sum_n in sum_results:
                return False
            # If not, add to set and re-iterate
            else:
                sum_results.add(sum_n)
                n_str = str(sum_n)
            
            # Check if we're at 1
            if sum_n == 1:
                return True

            
