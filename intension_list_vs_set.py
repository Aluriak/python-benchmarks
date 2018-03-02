"""Compare intention lists with condition on a set.

Result on my machine:

    First case: with complex set building notation
    integrated_complex 0.8994400080009655
    decoupled_complex 0.0014536359994963277

    Second case: with simple set building notation
    integrated_simple 0.00047374200039485004
    decoupled_simple 0.00047272700066969264

Therefore, it seems that sets in if expression are built at each loop.

"""


from timeit import timeit


print('First case: with complex set building notation')

def integrated_complex():
    N = 1000
    return [e for e in range(N) if e in {i for i in range(N) if i%2}]

def decoupled_complex():
    N = 1000
    s = {i for i in range(N) if i%2}
    return [e for e in range(N) if e in s]

for func in (integrated_complex, decoupled_complex):
    print(func.__name__, timeit(func, number=10))


print('\nSecond case: with simple set building notation')

def integrated_simple():
    N = 1000
    return [e for e in range(N) if e in {1, 2, 3, 4, 5}]

def decoupled_simple():
    N = 1000
    s = {1, 2, 3, 4, 5}
    return [e for e in range(N) if e in s]

for func in (integrated_simple, decoupled_simple):
    print(func.__name__, timeit(func, number=10))
