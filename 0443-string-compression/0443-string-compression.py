import math
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <2:
            return len(chars)

        i = 1
        current_count = 1
        left = 0

        while i < len(chars):
            if chars[i]==chars[i-1]:
                current_count += 1
                
            else:
                left += 1
                if current_count >1:
                    
                    for c in str(current_count):
                        chars[left] = c
                        left += 1
                    
                chars[left] = chars[i]
                current_count = 1

            i += 1



        left += 1
        if current_count>1:
            
            for c in str(current_count):
                chars[left] = c
                left += 1

        return left


            


        
        