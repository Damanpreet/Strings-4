"""
STEPS:
# Scan the string from left to right.
# If the character at index 0 is a "+"/"-" sign or a digit, proceed. Else, return 0.
# Strip the numbers from the string.
# Handle the edge cases for overflow.
# Return the digits as result.
"""
# Time complexity - O(n)
# Space complexity - O(1)
# Did this solution run on leetcode? - yes

class Solution:
    def myAtoi(self, str: str) -> int:   
        # strip any white space before the string.
        str = str.lstrip()
        
        # edge case
        if str=="": return 0
        
        # fetch the first character of the string.
        pos1 = str[0]
        
        # Return false if the character at position 1 is any other character than the digit/"+"/"-" sign.
        if not pos1.isdigit() and pos1!="+" and pos1!="-":
            return 0
        
        # find the sign of the number
        sign = "+"
        if pos1=="-":
            sign = "-"
        
        # define the integer maximum and
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        # find the digits from the string.
        digits = 0
        i = 0
        while i < len(str):
            ch = str[i]
            if ch.isdigit():
                # EDGE CASES
                # check if the digits are equal to the maximum number / 10
                if digits == INT_MAX//10:
                    if sign == "+" and (int(ch) >= 7 or digits >= INT_MAX):
                        return INT_MAX
                    elif sign == "-" and (int(ch) >= 8 or digits >= INT_MAX+1):
                        # print(digits, INT_MIN, digits >= INT_MIN)
                        return INT_MIN
                # check if the digits is greater.
                if digits > INT_MAX//10:
                    if sign == "+": return INT_MAX
                    else: return INT_MIN
                digits = digits*10 + int(ch)
            elif i!=0:  # do not break if the sign is "-" on index 0.
                break
            i+=1
            
        if sign == "-":
            return -digits
        return digits
        
        