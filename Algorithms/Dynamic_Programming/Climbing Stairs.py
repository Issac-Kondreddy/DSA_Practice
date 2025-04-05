#n stairs - one or two steps at one time
#no of ways we can climb

#tabulation
def climb_stairs_tab(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def climb_stairs_memo(n,memo={}):
    if n<=1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]


import time
start = time.time()
print(climb_stairs_tab(250))
end = time.time()
print(f"Time taken to calculate fib 250 using tabulation is {end-start}")


start = time.time()
print(climb_stairs_memo(250))
end = time.time()
print(f"Time taken to calculate fib 250 using memoization is {end-start}")
