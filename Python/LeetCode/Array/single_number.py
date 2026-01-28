class Solution:
    def singleNumber(self, nums):
        res=0
        for n in nums:
            res=n^res
        return res
    
lst=list(int(x) for x in input("Enter the Numbers with space: ").split())
sol=Solution()
print(sol.singleNumber(lst))