"""
This is a benchmark for a common operation on data : divide a stream
in two distinct parts.

Results on my computer:

    Data size: 10^1    Run number: 10^4
      | one: 1.07097e-06
      | two: 2.5132399999999998e-06
      | tee: 2.80146e-06
    Data size: 10^2    Run number: 10^3
      | one: 4.9237e-06
      | two: 1.61696e-05
      | tee: 1.61108e-05
    Data size: 10^3    Run number: 10^3
      | one: 3.91172e-05
      | two: 0.00013267019999999998
      | tee: 0.0001095443
    Data size: 10^4    Run number: 10^3
      | one: 0.0004593871
      | two: 0.0012987615
      | tee: 0.0010523339
    Data size: 10^5    Run number: 10^2
      | one: 0.007408312
      | two: 0.013263402
      | tee: 0.011219186999999999
    Data size: 10^6    Run number: 10^2
      | one: 0.077219024
      | two: 0.15086528700000001
      | tee: 0.113888637
    Data size: 10^7    Run number: 10^1
      | one: 0.73280142
      | two: 1.37809232
      | tee: 1.08570484


Obviously, usage of zip(*) (method one) is more efficient in all cases.

"""

import timeit
import itertools
from functools import partial


def one(data):
    return tuple(zip(*tuple(data)))

def two(data):
    ones, twos = [], []
    for one, two in data:
        ones.append(one)
        twos.append(two)
    return tuple(ones), tuple(twos)

def tee(data):
    def yield_n(it, index):
        return (elem[index] for elem in it)
    return tuple(yield_n(data, 0)), tuple(yield_n(data, 1))


for exponent_size, exponent_time in zip(range(1, 8), (4, 3, 3, 3, 2, 1, 1, 1)):
    data_size = 10**exponent_size
    print('Data size: 10^' + str(exponent_size), '   Run number: 10^' + str(exponent_time))
    data = tuple((1, 2) for _ in range(data_size))
    assert one(data) == two(data)
    assert one(data) == tee(data)
    for method in (one, two, tee):
        testtime = 10**exponent_time
        runtime = round(timeit.timeit(partial(method, data), number=testtime), 7)
        print('  | '+method.__name__+':', runtime / testtime)
