#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        length = 0
        alphabets = set(s)
        for alphabet in alphabets:
            count = s.count(alphabet)
            # 문자열 내에서 같은 알파벳이 3개 이상 존재할 수 없으므로
            # 알파벳의 갯수가 짝수인 경우 2개가, 홀수인 경우 1개가 남을 것이다.
            length += 1 if count % 2 else 2
        return length
# @lc code=end
