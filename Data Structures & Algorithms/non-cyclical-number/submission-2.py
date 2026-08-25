class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        sum_results = set()

        while True:
            sum_n = 0
            for str_digit in n_str:
                sum_n += int(str_digit) ** 2
            if sum_n in sum_results:
                return False
            else:
                sum_results.add(sum_n)
                n_str = str(sum_n)
            if sum_n == 1:
                return True

            
