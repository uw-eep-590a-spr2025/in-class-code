

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)



def fib_cache_helper(n, cache):
    print(f'{n}: {cache}')

    if cache[n] == None:
        cache[n] = (fib_cache_helper(n-1, cache) +
                    fib_cache_helper(n-2, cache))
    return cache[n]


def fib_cache(n):
    results = [None] * (n + 1)
    results[0] = 0
    results[1] = 1
    # results = {str(0): 0, str(1): 1}
    if not results[n]:
        return fib_cache_helper(n, results)

def fib_dp(n):
    results = [None] * (n + 1)
    results[0] = 0
    results[1] = 1

    for i in range(2, n + 1):
        print(results)
        results[i] = results[i-1] + results[i-2]

    return results[n]


print(fib_dp(40))


