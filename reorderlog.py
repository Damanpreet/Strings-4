"""
# Custom comparator rules :
# 1 - return a negative value (< 0) when the left item should be sorted before the right item.
# 2 - return a positive value (> 0) when the left item should be sorted after the right item.
# 3 - return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence.

# We can sort using key without cmp_to_sort. When we are checking the distance.
# Use cmp_to_sort while comparing distinct values. In this case, characters and digits.
"""
# Time complexity - O(n logn*m) where m is the length of the string.
# Space complexity - O(m*n) -- Timsort in python uses O(n) extra space (not inplace)
# Did this solution run on leetcode? - yes

from functools import cmp_to_key 
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def compare(log1, log2):
            # 1 - split the log based on space
            # separate the identifier and the characters.
            logSplit1 = log1.split(" ", 1)
            logSplit2 = log2.split(" ", 1)
            
            # find the identifier
            identifier1 = "dig" if logSplit1[1][0].isdigit() else "let"
            identifier2 = "dig" if logSplit2[1][0].isdigit() else "let"
            
            """
                # case 1 - when first is a digit log, second is a letter log.
                # 2 - Reorder such that letter logs come before any digit logs.
                # case 3 - both digit logs
            """
            if identifier1 == "dig" and (identifier2 == "let" or identifier2 == "dig"):
                return 1
            
            elif identifier1 == "let" and identifier2 == "let":
                """
                # case 2 - both are letters
                # 3 - Letter logs are lexicographically ordered.
                # 4 - Reorder based on ties in case of ties.
                """
                if log1 == log2:
                    return 1 if logSplit1[0] > logSplit2[0] else -1
                else:
                    return 1 if logSplit1[1] > logSplit2[1] else -1
                
            else: 
                """
                # case 4 - when first is a digit log, second is a letter log.
                """
                return -1
            
        return sorted(logs, key=cmp_to_key(compare))
    

"""
    Leetcode solution:
    
    By defining a custom key sort.
    
    Return a tuple with values (key, log string, identifier)
    key - 1 if digit else 0 
    This makes sure that the values are sorted by key first followed by log string and then the identifier.
    
    For digit-
    Return (1, ) and blanks for log string and identifier.
    This makes sure that digits are considered in the order in which they appear in the input string. Timsort is a stable algorithm.
"""
# Time complexity - O(n logn*m) where m is the length of the string.
# Space complexity - O(m*n) -- Timsort in python uses O(n) extra space (not inplace)
# Did this solution run on leetcode? - yes

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare(log):
            identifier, logstr = log.split(" ", 1)
            return (0, logstr, identifier) if logstr[0].isalpha() else (1,)
        
        return sorted(logs, key=compare)
        