from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    def binSearch(self, nums: List[int], target: int, leftBias: bool) -> int:
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1  # continue searching left
                else:
                    l = m + 1  # continue searching right
        return i

# --- Driver code to run and test the function ---

if __name__ == "__main__":
    # Example input
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # Create an instance of the Solution class
    solution = Solution()

    # Call the method and print the result
    result = solution.searchRange(nums, target)
    print("First and last position of", target, ":", result)
