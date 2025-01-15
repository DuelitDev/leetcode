#
# @lc app=leetcode id=2429 lang=python3
#
# [2429] Minimize XOR
#
# https://leetcode.com/problems/minimize-xor/description/
#
# algorithms
# Medium (44.71%)
# Likes:    697
# Dislikes: 44
# Total Accepted:    53.7K
# Total Submissions: 98.5K
# Testcase Example:  '3\n5'
#
# Given two positive integers num1 and num2, find the positive integer x such
# that:
# 
# 
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# 
# 
# Note that XOR is the bitwise XOR operation.
# 
# Return the integer x. The test cases are generated such that x is uniquely
# determined.
# 
# The number of set bits of an integer is the number of 1's in its binary
# representation.
# 
# 
# Example 1:
# 
# 
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3
# = 0 is minimal.
# 
# 
# Example 2:
# 
# 
# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1
# = 2 is minimal.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num1, num2 <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = num1.bit_count()
        b = num2.bit_count()
        # 만약 num1의 1비트 수가 num2의 1비트 수보다 많다면
        if (a > b):
            i = 1
            while a != b:
                if num1 & i:  # 1비트를 찾아
                    a -= 1
                    num1 &= ~i  # 0비트로 변경
                i <<= 1
            return num1
        # 만약 num1의 1비트 수가 num2의 1비트 수보다 적다면
        elif (a < b):
            i = 1
            while a != b:
                if not num1 & i:  # 0비트를 찾아
                    a += 1
                    num1 ^= i  # 1비트로 변경
                i <<= 1
            return num1
        # 만약 num1, num2의 1비트 수가 같다면
        else:
            return num1
# @lc code=end