class Solution:
    def longestPalindrome1(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2:
            return s
        start, max_len = 0, 0
        i = 0
        while i < s_len:
            if s_len - i <= max_len/2:
                break
            left = right = i
            while right < s_len-1 and s[right] == s[right+1]:
                right += 1
            while left >= 0 and right < s_len and s[left] == s[right]:
                left -= 1
                right += 1
            cur_len = right - left - 1
            if max_len < cur_len:
                max_len = cur_len
                start = left + 1
            i+= 1
        return s[start:start+max_len]

    ## dp:
    ## dp[i][j] = 1 i == j
    ##  = s[i] == s[j] j=i+1
    ##  = s[i] == s[j] && dp[i+1][j-1] j>i+1
    def longestPalindrome2(self, s:str)->str:
        s_len = len(s)
        dp = [[0 for _ in range(s_len)] for _ in range(s_len)]
        max_len = 0
        start = 0
        for i in range(s_len):
            dp[i][i] = 1
            for j in range(0, i):
                if s[i] == s[j] and (i==j+1 or dp[j+1][i-1] == 1):
                    dp[j][i] = 1
                if dp[j][i] == 1 and max_len < i-j+1:
                    max_len = i-j+1
                    start = j
        return s[start:start+max_len]


s =  "babad"
# s = "bb"
print(Solution().longestPalindrome2(s))

class Solution1:
    def reverse_z(self, s:str, numRows:int):
        s_len = len(s)
        if s_len <= numRows or numRows == 1:
            return s
        half_z = (2*numRows-2)
        nCols = s_len // half_z*(numRows-1)
        lefts = s_len % half_z 
        nCols += lefts % numRows + 1 if lefts > 0 else 0
        showArr = [[None for _ in range(nCols)] for _ in range(numRows)]
        i = 0
        row, col = 0, 0
        while i < s_len:
            all_per = i // half_z
            while i // half_z == all_per and i < s_len:
                left = i % half_z
                if not left // numRows:
                    row = left % numRows
                else:
                    col += 1
                    row = (numRows-2-left % numRows)
                print(row, col, i, s_len, numRows, nCols)
                showArr[row][col] = s[i]
                i += 1
            col += 1
        res = ""
        for i in range(numRows):
            for j in range(nCols):
                if showArr[i][j] is not None:
                    res+=showArr[i][j]
        return res

    def reverse_z1(self, s:str, numRows:int)->str:
        s_len = len(s)
        if s_len <= numRows or numRows == 1:
            return s 
        
        z_len = (2*numRows-2)
        res = ""
        for i in range(numRows):
            for j in range(i, s_len, z_len):
                res += s[j]
                middle = j + z_len - 2*i
                if i != 0 and i != (numRows-1) and middle < s_len:
                    res += s[middle]
        return res

    def reverse_z2(self, s:str, numRows:int)->str:
        s_len = len(s)
        if s_len <= numRows or numRows == 1:
            return s
        new_s = [""] * numRows
        s_p = 0
        while s_p < s_len:
            for i in range(numRows):
                if s_p >= s_len:
                    break
                new_s[i] += s[s_p]
                s_p += 1
            for i in range(numRows-2, 0, -1):
                if s_p >= s_len:
                    break
                new_s[i] += s[s_p]
                s_p += 1
        res = "".join(new_s)
        return res

s = "LEETCODEISHIRING"; numRows = 3
res = "LCIRETOESIIGEDHN"
# s = "PAYPALISHIRING"
# numRows = 3
# s = "AB"
# numRows = 1
print(Solution1().reverse_z2(s, numRows)==res)





            
