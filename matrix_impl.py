"""
Benchmarks showing that matrixes as list are more efficient than dict
implementation counterparts, for both building and access.


TODO:
- test different building methods (without intension syntax)
- test speed for iteration over full data

5 × 5
	as_list_build: 0.004905984000288299
	as_dict_build: 0.0051451720000841306
	access list (2;4): 0.00022962999992159894
	access dict (2;4): 0.00027621699973678915
	access list (0;1): 0.00022561900004802737
	access dict (0;1): 0.00027637700077320915
	access list (4;1): 0.00022410099973058095
	access dict (4;1): 0.0002736019996518735
	access list (2;1): 0.00022972700026002713
	access dict (2;1): 0.00027363600020180456
	access list (0;1): 0.00022476899994217092
	access dict (0;1): 0.00027600799967331113
	access list (4;1): 0.0002238749993921374
	access dict (4;1): 0.0002738029997999547
	access list (4;3): 0.00022766900019632885
	access dict (4;3): 0.00027182000030734343
	access list (1;0): 0.0002268010002808296
	access dict (1;0): 0.0002760719999059802
50 × 50
	as_list_build: 0.14956806000009237
	as_dict_build: 0.28228116700029204
	access list (29;34): 0.00018884899964177748
	access dict (29;34): 0.00022596300004806835
	access list (25;14): 0.0001847160001489101
	access dict (25;14): 0.0002584429994385573
	access list (0;22): 0.0001988240001082886
	access dict (0;22): 0.0002389110004514805
	access list (7;14): 0.00019908099966414738
	access dict (7;14): 0.00023805499949958175
	access list (34;2): 0.0001851819997682469
	access dict (34;2): 0.00022615699981543003
	access list (22;34): 0.00020264599970687414
	access dict (22;34): 0.00022416599949792726
	access list (42;38): 0.00020015800055261934
	access dict (42;38): 0.0002456090005580336
	access list (47;19): 0.00019953399987571174
	access dict (47;19): 0.000258367999776965
500 × 500
	as_list_build: 15.645348737999484
	as_dict_build: 98.41559852899991
	access list (431;23): 0.0002347390000068117
	access dict (431;23): 0.0002975010002046474
	access list (324;10): 0.0002382889997534221
	access dict (324;10): 0.0002961789996334119
	access list (152;41): 0.00023367299945675768
	access dict (152;41): 0.0002862800001821597
	access list (494;379): 0.00023275699913938297
	access dict (494;379): 0.00030911800058675
	access list (326;327): 0.00023407199932989897
	access dict (326;327): 0.00030683599925396265
	access list (94;251): 0.0002337970008738921
	access dict (94;251): 0.00028192499939905247
	access list (420;0): 0.000235366999731923
	access dict (420;0): 0.0003015849997609621
	access list (454;36): 0.00023336599952017423
	access dict (454;36): 0.0002958049999506329

"""


import random
from timeit import timeit
from functools import partial

timeit = partial(timeit, number=1000)


def as_list_build(row, col):
    return [[i*j for i in range(col)] for j in range(row)]
def as_dict_build(row, col):
    return {(i, j): i*j for i in range(row) for j in range(col)}


def as_list_access(mat, row, col) -> int:
    return mat[row][col]
def as_dict_access(mat, row, col) -> int:
    return mat[row, col]


if __name__ == "__main__":
    TESTED_DIMS = [(5, 5), (50, 50), (500, 500)]
    for nb_row, nb_col in TESTED_DIMS:
        print('{} × {}'.format(nb_row, nb_col))
        for method in (as_list_build, as_dict_build):
            print('\t'+method.__name__ + ':', timeit(lambda: method(nb_row, nb_col)))

        matlist, matdict = as_list_build(nb_row, nb_col), as_dict_build(nb_row, nb_col)
        for _ in range(8):
            i, j = random.randrange(0, nb_row), random.randrange(0, nb_col)
            assert as_dict_access(matdict, i, j) == as_list_access(matlist, i, j)
            print('\taccess list ({};{}):'.format(i, j), timeit(lambda: as_list_access(matlist, i, j)))
            print('\taccess dict ({};{}):'.format(i, j), timeit(lambda: as_dict_access(matdict, i, j)))
