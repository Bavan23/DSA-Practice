class Solution(object):
    def twoSum(self, nums, target):
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return
        
ob1=Solution()
list1=list(map(int,input("List ").split()))
target=int(input())
result = ob1.twoSum(list1,target)
print(result)  