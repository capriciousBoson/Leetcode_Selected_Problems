class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1,n):
            # print(f"cas at {i} : {res}")

            ans = ""
            char = res[0]
            count = 1

            for i in range(1,len(res)):
                if res[i]==char:
                    count += 1
                else:
                    ans = ans+ str(count)  + char 
                    char = res[i]
                    count = 1
            ans = ans + str(count)  + char 
            res = ans

        return res