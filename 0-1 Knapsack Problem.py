import math


class Knapsack:
    def __init__(self,weight, value):
        # Including a dummy val to map 'n' with index
        self.weight = [-math.inf] + weight
        self.value = [-math.inf] + value

    def naive_knapsack(self, n, C):
        if n == 0 or C == 0:
            result = 0
        elif self.weight[n] > C:
            result = self.naive_knapsack(n-1, C)
        else:
            excluded = self.naive_knapsack(n-1, C)
            included = self.value[n] + self.naive_knapsack(n-1, C - self.weight[n])
            result = max(excluded, included)
        return result

    def dp_knapsack(self, n, C):
        dp = [[0 for _ in range(n+1)] for __ in range(C+1)]

        # Building up DP table in bottom-up manner
        for count in range(n+1):
            for cap in range(C+1):
                if count == 0 or cap == 0:
                    dp[cap][count] = 0
                elif self.weight[count] > cap:
                    dp[cap][count] = dp[cap][count-1]
                else:
                    excluded = dp[cap][count-1]
                    included = self.value[count] + dp[cap - self.weight[count]][count-1]
                    dp[cap][count] = max(excluded, included)

        return dp[C][n]







val = [60, 100, 120]
val2 = [10,20,30]
wt = [10, 20, 30]
wt2 = [1,1,1]
W = 50
W2 = 2
n = len(val)
n2 = len(val2)
kp = Knapsack(wt, val)
print(kp.naive_knapsack(n, W))
print("==========")
print(kp.dp_knapsack(n, W))

print("======================================================================")

kp2 = Knapsack(wt2, val2)
print(kp2.naive_knapsack(n2, W2))
print("==========")
print(kp2.dp_knapsack(n2, W2))


