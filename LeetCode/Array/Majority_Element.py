from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0  # Initialize result (res) and count

        for n in nums:  # Loop through each number in the array
            if count == 0:  
                res = n  # Set new candidate
            count += (1 if n == res else -1)  # Increase or decrease count
        
        return res  # Return the majority element
    

#approach 2
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res,maxCount=0,0
        for n in nums:
            count[n] = count.get(n,0) + 1
            res= n if count[n]>maxCount else res
            maxCount = max(maxCount,count[n])
        return res
"""

# Example Usage:
if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]  # Sample input
    solution = Solution()  # Create an instance of Solution class
    result = solution.majorityElement(nums)  # Call the function
    print("Majority Element:", result)  # Print the result
