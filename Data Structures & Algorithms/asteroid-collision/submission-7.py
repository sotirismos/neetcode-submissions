class Solution:

        
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final_state = []
        for ast in asteroids:
            append = True
            while final_state and ast < 0 and final_state[-1] > 0:
                if abs(final_state[-1]) > abs(ast):
                    append = False
                    break
                elif abs(final_state[-1]) == abs(ast):
                    final_state.pop(-1)
                    append = False
                    break
                else:
                    final_state.pop(-1)
            if append:
                final_state.append(ast)
        
        return final_state