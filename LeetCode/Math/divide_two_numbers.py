class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        quotient = -quotient if negative else quotient
        return quotient

# Main function to test the code
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (10, 3),
        (7, -3),
        (-10, -2),
        (-2147483648, -1),
        (0, 1)
    ]
    
    for dividend, divisor in test_cases:
        result = solution.divide(dividend, divisor)
        print(f"divide({dividend}, {divisor}) = {result}")

if __name__ == "__main__":
    main()
