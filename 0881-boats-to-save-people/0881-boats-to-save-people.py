class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0

        while l <r:
            combined_weight = people[l] + people[r]
            if combined_weight <= limit:
                l += 1
                r -= 1
            else:
                r -=1
            boats += 1
        
        if l==r:
            boats += 1
        return boats
            

        