def climbStairs(n):
    prev = 1
    prev2 = 0
    for i in range(1, n + 1):
        curi = prev + prev2
        prev2 = prev
        prev = curi
    return prev
n = 5
print(climbStairs(n))
#https://leetcode.com/problems/climbing-stairs/description/