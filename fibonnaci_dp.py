def my_fib(x, memo=dict()):
    if memo.get(x):
         return memo[x]
    if x == 1 or x == 2:
         result = 1
    else:
         result = my_fib(x - 1, memo) + my_fib(x -2, memo)
    memo[x] = result
    return result


n = 8
print(my_fib(n))