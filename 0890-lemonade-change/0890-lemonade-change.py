class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_counts = {5:0, 10:0, 20:0}
        total_bills = 0
        
        for amount in bills:
            bill_counts[amount] += 1
            total_bills += 1
            
            if amount>5:
                change = amount-5

                while change and total_bills:
                    if change >=10 and bill_counts[10]:
                        change-=10
                        bill_counts[10] -=1
                        total_bills -=1
                    elif change>=5 and bill_counts[5]:
                        change -= 5
                        bill_counts[5] -=1
                        total_bills -=1
                    else:
                        return False
                if change:
                    return False
        return True



                        

            
                
 
        