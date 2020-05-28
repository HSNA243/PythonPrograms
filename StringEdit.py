s1 = input()
s2 = input()
m = len(s1)
n = len(s2)
dp = [[-1 for x in range(m+1)] for x in range(n+1)] 
for i in range(n+1):
    for j in range(m+1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1]+1 , dp[i][j-1]+1 , dp[i-1][j]+1)
print("Answer is:",dp[n][m])