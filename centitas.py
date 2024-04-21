def CountWays(n, dp):

    if n < 0:
        return 0
    elif n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = CountWays(n-1, dp) + CountWays(n-2, dp) + CountWays(n-12, dp) + CountWays(n-40, dp)
    return dp[n]

n = 856
dp = [-1]*(n+1)
print("Number of ways = " + str(CountWays(n, dp)))