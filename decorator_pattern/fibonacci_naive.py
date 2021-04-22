# Non performatic version
#def fibonacci(n):
#    assert(n >= 0), 'n must be >= 0'
#    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

# Performatic version
#known = {0:0, 1:1}
#def fibonacci(n):
#    assert(n >= 0), 'n must be >= 0'
#    if n in known:
#        return known[n]
#    res = fibonacci(n-1) + fibonacci(n-2)
#    known[n] = res
#    return res

# The new version is performatic, but if we apply this to all functions 
# in our program, will be a mess. That's when decorators are useful

'''Em computação, memoization ou memoisation é uma técnica de otimização 
usado principalmente para acelerar programas de computador, armazenando 
os resultados de chamadas de função caros e retornando o resultado em 
cache quando as mesmas entradas ocorrer novamente.
'''

# --------------------------------
import functools

def memoize(fn):
    '''Memoize decorator'''
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer

@memoize
def nsum(n):
    '''Returns the sum of the first n numbers'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)

@memoize
def fibonacci(n):
    '''Returns the nth number of the Fibonacci sequence'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    # First example
    from timeit import Timer
    #t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
    #print(t.timeit())
    # -------------
    measure = [ {'exec':'fibonacci(100)', 'import':'fibonacci',
    'func':fibonacci},{'exec':'nsum(200)', 'import':'nsum',
    'func':nsum} ]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time:{}'.format(m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit()))