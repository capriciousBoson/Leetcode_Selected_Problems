from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize < 2: return True
        n = len(hand)

        if n%groupSize !=0 : return False
        c = Counter(hand)
        min_heap = []
        for card, count in c.items():
            heapq.heappush(min_heap, [card, count])
        
        hand_count = 0
        while min_heap:
            # print(f"\ncurrent heap : {min_heap} | hand_count : {hand_count}")
            if hand_count==0 or hand_count==groupSize:
                card, card_count = heapq.heappop(min_heap)

                card_count -= 1
                prev_card = card

                hand_count = 1
                pushback = []

                # print(f"hand ({hand_count}) : {prev_card}")

                while min_heap:
                    next_card, next_card_count = heapq.heappop(min_heap)
                    if next_card == prev_card+1:
                        next_card_count -= 1
                        prev_card = next_card
                        hand_count += 1
                        # print(f"hand ({hand_count}) : {next_card}")

                        if next_card_count:
                            pushback.append([next_card, next_card_count])

                        if hand_count == groupSize:
                            break

                        
                            
                    else:
                        pushback.append([next_card, next_card_count])
                        if  next_card > prev_card+1:
                            break

                if card_count:
                    heapq.heappush(min_heap, [card, card_count])
                for x in pushback:
                    heapq.heappush(min_heap, x)

            else:
                return False
        return hand_count==groupSize







            