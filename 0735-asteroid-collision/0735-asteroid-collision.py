class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for a in asteroids:
            add = True
            while stk and stk[-1]>0 and a < 0:
                ngh = stk[-1]
                if abs(ngh) == abs(a) :
                    stk.pop()
                    add = False
                    break
                elif abs(ngh) < abs(a):
                    stk.pop()
                elif abs(ngh) > abs(a):
                    add = False
                    break
            if add:
                stk.append(a)
        return stk

            
        