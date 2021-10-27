import math
n = int(input())
dp=[0 for _ in range(n+1)] #[0,0,...,0] 총 x+1개
for i in range(2,n+1):
    one, two, three = math.inf, math.inf, dp[i-1]
    if i%3 == 0: 
        one = dp[i//3]
    if i%2 == 0:
        two = dp[i//2]
    dp[i]= 1+min(one,two,three)
print(dp[n])