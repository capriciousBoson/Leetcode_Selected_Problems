class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        if groupSize < 2: return True

        cards = collections.Counter(hand)
        minHeap = list(cards.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
    
            freq = cards[start]

            if freq > 0:

                for n in range(start, start+groupSize ):
                    cards[n] -= freq
                    if cards[n] < 0:
                        return False
            else:
                heapq.heappop(minHeap)
        return True


        