""" A Naive recursive Python program to fin minimum number """
def editDistance(str1, str2, m , n):
    if m==0:
         return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )

def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]
str1 = raw_input("Enter first string")
str2 = raw_input("Enter second string")
print "Naive Solution :"
print editDistance(str1, str2, len(str1), len(str2))
print "Dynamic Solution"
print editDistDP(str1, str2, len(str1), len(str2))
