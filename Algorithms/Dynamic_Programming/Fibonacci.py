#Return nth fibonacci Series
import time
def fib_tab(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fib_memo(n, memo={}):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo)+fib_memo(n-2, memo)
    return memo[n]

start = time.time()
print(fib_tab(250))
end = time.time()
print(f"Time taken to calculate fib 250 using tabulation is {end-start}")


start = time.time()
print(fib_memo(250))
end = time.time()
print(f"Time taken to calculate fib 250 using memoization is {end-start}")
