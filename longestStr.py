##159, 340 the same 2 replace with k
class Solution:
    def lengthOfLongestSubstringTwoDistinct1(self, s:str)->int:
        # from collections import deque
        if len(s) <= 2:
            return len(s)
        end_loc = {}
        maxlen = 0
        chars = set()
        left, right = 0, 0
        while right < len(s):
            chars.add(s[right])
            end_loc[s[right]] = right
            right += 1
            if len(chars) > 2:
                this_len = right - left - 1
                if this_len > maxlen:
                    maxlen = this_len
                left_char = s[left]
                chars.remove(left_char)
                left = end_loc[left_char] + 1
        if len(chars) <=2 and maxlen > (right-left):
            maxlen = this_len
        return maxlen

    def lengthOfLongestSubstringTwoDistinct(self, s:str)->int:
        if len(s) <= 2:
            return len(s)
        end_loc = {}
        maxlen = 0
        left, right = 0, 0
        while right < len(s):
            end_loc[s[right]] = right
            while len(end_loc) > 2:
                # if end_loc[s[left]] == left:
                #     del end_loc[s[left]]
                # left += 1
                remove_key = s[left]
                left = end_loc[s[left]] + 1
                del end_loc[remove_key]
            maxlen = max(maxlen, right-left+1)
            right += 1
        return maxlen

    def lengthOfLongestSubstringKDistinct(self, s:str, k:int)->int:
        from collections import defaultdict
        if len(s) < k:
            return len(s)
        end_loc = defaultdict(int)
        maxlen = 0
        left, right = 0, 0
        while right < len(s):
            end_loc[s[right]] += 1
            while len(end_loc) > 2:
                end_loc[s[left]] -= 1
                if end_loc[s[left]] == 0:
                    del end_loc[s[left]]
                left += 1
            maxlen = max(maxlen, right-left+1)
            right += 1
        return maxlen




# s = "eceba"
s = "ccaabbb"
print(Solution().lengthOfLongestSubstringTwoDistinct(s))
print(Solution().lengthOfLongestSubstringKDistinct(s, k=2))