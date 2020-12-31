INT_MAX = 2 ** 31 - 1
INT_MIN = - 2**31
# 8
class Solution:
    def myAtoi(self, s: str)->int:
        if s.isspace():
            return 0
        s_len, i, res, sign = len(s), 0, 0, 1
        while i < s_len and s[i] == " ":
            i +=1
        if i < s_len and s[i] in ["+", "-"]:
            sign = 1 if s[i] == "+" else -1
            i += 1
        while i < s_len and s[i] >= "0" and s[i] <= "9":
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and s[i] -"0" > 7):  ## INT_MAX: 2**31-1
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + int(s[i])
            i += 1
        return res*sign

s = "42"
# s = "      -42"
# s = "4193 with words"
# s = "words with 987"
# s = "-91283472332"
print(Solution().myAtoi(s))

#  7
class Solution1:
    def reverse(self, x:int):
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            if x > INT_MAX:
                return 0
            res = res * 10 + x % 10
            x = x // 10
        return res * sign

print(Solution1().reverse(-321))


# 150
class Solution2:
    def isNumber(self, s:str)->bool:
        s_len = len(s)
        left, right =0, s_len-1
        while left < s_len and s[left] == " ":  left += 1
        while right > 0 and s[right] == " ": right -= 1
        s = s[left:right+1]

        e_cnt, dot_cnt, e_pos, dot_pos = 0, 0, 0, 0
        for idx, item in enumerate(s):
            if item == "e": e_cnt += 1; e_pos = idx
            elif item == ".": dot_cnt += 1; dot_pos = idx
            elif (item >="0" and item <="9") or item in ["+", "-"]: pass
            else: print(item); return False
        if e_cnt > 1 or dot_cnt > 1 or (e_cnt ==1 and dot_cnt == 1 and dot_pos > e_pos):
            return False
        if e_cnt != 0:
            bef_exp = s[:e_pos]
            aft_exp = s[e_pos+1:]

            return (len(bef_exp) == 0 or self.check_num(bef_exp)) and self.check_num(aft_exp)
        else:
            return self.check_num(s)

    def check_num(self, s:str)->bool:
        # "dot is already checked"
        if len(s) > 0 and (s[0] in ["+", "-"]):
            s = s[1:]
        if len(s) <= 0: return False
        if s == ".": return False
        if s.find('+')!=-1 or s.find('-')!=-1: return False
        return True
            
s = "-54.53061"
s="+1.e+5"
s="+.8"
s="-."
s="e9"
s="4e+"
s="1+e"
s="2e10"
print(Solution2().isNumber(s))

# 9
class Solution3:
    def isPalindrome(self, x:int):
        if x < 0 or x % 10 == 0 and x !=0:
            return False
        reverNum = 0
        originNum = x
        while x != 0:
            if reverNum > INT_MAX // 10: return False
            reverNum = reverNum * 10 + x % 10
            x /= 10
        return reverNum == originNum

    def isPalindrome1(self, x:int):
        if x < 0 or x % 10 == 0 and x !=0:
            return False
        reverNum = 0
        while x > reverNum:
            reverNum = reverNum * 10 + x % 10
            x /= 10
        return reverNum // 10 == x or x == reverNum ## odd or even


# 10
class Solution4:
    def isMatch(self, s:str, p:str)->bool:
        if len(p) == 0: return len(s) == 0
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or ((s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p))
        else:
            return len(s) != 0 and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:])
            
    ### dp p[i][j] represent s[0,i), p[0, j)
    ## p[i][j] = p[i-1][j-1] (p[j-1]!='*' and p[j-1] == s[i-1] or p[j-1] == ".")
    ## p[i][j] = p[i][j-2]   (p[j-1]=='*' and p[j-2] does not match any in s)
    ## p[i][j] = p[i-1][j] and p[j-2] == s[i-1] or p[j-2] == "."  (p[j-1]=='*' and p[j-2] match in s >= 1)
    def isMatch_dp(self, s:str, p:str)->bool:
        s_len = len(s)
        p_len = len(p)
        dp = [[False for _ in range(p_len+1)] for _ in range(s_len+1)]
        dp[0][0] = True
        for i in range(p_len+1):
            for j in range(1, s_len+1):
                if j > 1 and p[j-1]=='*':
                    dp[i][j] = dp[i][j-2] | ( i > 0 & (s[i-1] == p[j-2] | p[j-2] == '.'))
                else:
                    dp[i][j] = (i > 0 & dp[i-1][j-1] & (p[j-1] == s[i-1] or p[j-1] == '.'))
        return dp[s_len][p_len]


s = "aa"; p = "aaaa"
print(Solution4().isMatch_dp(s, p))





        