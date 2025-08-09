from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize < 2: return True

        if len(hand)%groupSize :
            return False
        counts = Counter(hand)
        mh = list(counts.keys())
        heapq.heapify(mh)

        while mh:
            start = mh[0]
            for x in range(start, start+groupSize):
                if not counts[x]:
                    return False
                counts[x] -=1
                if counts[x]==0 :
                    if x != mh[0]:
                        return False
                    heapq.heappop(mh)
        return True








            