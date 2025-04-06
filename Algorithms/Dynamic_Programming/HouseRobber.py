def house_robber(nums):
    dp = [0]*(len(nums)+1)
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[len(nums)-1]


nums = [2, 7, 9, 3, 1]
print(house_robber(nums))

