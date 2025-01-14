#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
#
# algorithms
# Medium (79.76%)
# Likes:    725
# Dislikes: 37
# Total Accepted:    110.2K
# Total Submissions: 129K
# Testcase Example:  '[1,3,2,4]\n[3,1,2,4]'
#
# You are given two 0-indexed integer permutations A and B of length n.
# 
# A prefix common array of A and B is an array C such that C[i] is equal to the
# count of numbers that are present at or before the index i in both A and B.
# 
# Return the prefix common array of A and B.
# 
# A sequence of n integers is called a permutation if it contains all integers
# from 1 to n exactly once.
# 
# 
# Example 1:
# 
# 
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
# 
# 
# Example 2:
# 
# 
# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= A.length == B.length == n <= 50
# 1 <= A[i], B[i] <= n
# It is guaranteed that A and B are both a permutation of n integers.
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a, b = set(), set()
        temp = []
        for i in range(len(A)):
            # A와 B를 각각 집합에 차근차근 추가하면서
            a.add(A[i])
            b.add(B[i])
            # 그 교집합의 원소의 갯수를 리스트에 추가
            temp.append(len(a & b))
        return temp
# @lc code=end

