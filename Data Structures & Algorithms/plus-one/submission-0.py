class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer_str_list = []
        for integer in digits:
            integer_str_list.append(str(integer))
        integer_str = "".join(integer_str_list)
        integer_int = int(integer_str)

        integer_int += 1

        integer_str = str(integer_int)
        integer_int_list = []
        for char in integer_str:
            integer_int_list.append(int(char))
        return integer_int_list