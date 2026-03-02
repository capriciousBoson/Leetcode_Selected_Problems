class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        i = 0
        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                    continue
            for idx in range(3):
                if triplet[idx]==target[idx]:
                    found[idx] = True
            
            if all(found): return True

        return all(found)

                