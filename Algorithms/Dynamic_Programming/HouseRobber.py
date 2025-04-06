import time

#tabulation method
def house_robber_tab(nums):
    dp = [0]*(len(nums))
    if len(nums)==1:
        return nums[0]
    if len(nums)==0:
        return 0
    dp[0], dp[1] =  nums[0],max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    return dp[len(nums)-1]


#Memoization
def house_robber_memo(nums, n,memo={}):
    if n<0:
        return 0
    if n==0:
        return nums[0]
    if n==1:
        return max(nums[0], nums[1])
    else:
        memo[n] = max(house_robber_memo(nums, n-1, memo), nums[n] + house_robber_memo(nums,n-2, memo))
        return memo[n]

nums = [2,7,9,3,1]
start = time.time()
print(house_robber_tab(nums))
end = time.time()
print("Time Taken by tabulation: ",end-start)
start = time.time()
print(house_robber_memo(nums, len(nums)-1))
end = time.time()
print("Time Taken by memoization: ",end-start)

