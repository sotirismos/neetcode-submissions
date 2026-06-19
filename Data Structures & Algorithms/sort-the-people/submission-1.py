class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        sorted_by_height = sorted(zip(heights, names), reverse=True)
        for height, name in sorted_by_height:
            res.append(name)
        return res