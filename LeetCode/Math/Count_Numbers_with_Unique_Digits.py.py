from typing import List

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Base case
        if n == 0:
            return 1  # Only "0" is valid
        
        count = 10  # For n = 1 (Numbers: 0-9)
        unique_digits = 9  # First digit has 9 choices (1-9)
        available_choices = 9  # Second digit has 9 choices (0-9 except first)

        for i in range(2, n + 1):
            unique_digits *= available_choices  # Compute permutation
            count += unique_digits  # Add to total count
            available_choices -= 1  # Reduce available choices

        return count

# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [0, 1, 2, 3, 4, 5]

    for n in test_cases:
        result = solution.countNumbersWithUniqueDigits(n)
        print(f"n = {n}, Unique Numbers Count = {result}")
