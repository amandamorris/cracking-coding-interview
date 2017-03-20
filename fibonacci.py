def fibonacci(n):
    # Write your code here.
    cache = {0:0, 1:1}
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


print fibonacci(10)
# fibonacci(6)
