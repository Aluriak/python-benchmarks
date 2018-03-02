"""Efficiency of arguments transmission methods.

Results on my computer:

No argument handling
| With args as tuple
  | explicit_args: 2.7854394240002875
  | implicit_args: 2.7681000799993853
| With args as keywords
  | explicit_args: 0.4937617830000818
  | implicit_kwargs: 0.008441988000413403
With argument handling
| With args as tuple
  | explicit_args_returned: 3.4448003190000236
  | implicit_args_returned: 2.7597104570004376
| With args as keywords
  | explicit_args_returned: 0.4947863650004365
  | implicit_kwargs_returned: 0.008351686999958474


"""
import itertools
from timeit import timeit

# a0, a1, b0,…
MAX_ARGS = 255  # defined by Python
ARGS = tuple(map(''.join, itertools.product('abcdefghijklmnopqrstuvwxyz', map(str, range(10)))))[:MAX_ARGS]


# Build tested functions
exec('''
def explicit_args({args}): return
def explicit_args_returned({args}): return {args}
'''.format(args=', '.join(ARGS)))

def implicit_args(*args): return
def implicit_args_returned(*args): return args
def implicit_kwargs(**args): return
def implicit_kwargs_returned(**args): return args


print('No argument handling')
print('| With args as tuple')
for function in (explicit_args, implicit_args):
    args_values = range(len(ARGS))
    print('  | '+function.__name__ + ':', timeit(lambda: function(*args_values)))
print('| With args as keywords')
for function in (explicit_args, implicit_kwargs):
    args_values = dict(zip(ARGS, range(len(ARGS))))
    print('  | ' + function.__name__ + ':', timeit(lambda: function(**args_values), number=1000))


print('With argument handling')
print('| With args as tuple')
for function in (explicit_args_returned, implicit_args_returned):
    args_values = range(len(ARGS))
    print('  | '+function.__name__ + ':', timeit(lambda: function(*args_values)))
print('| With args as keywords')
for function in (explicit_args_returned, implicit_kwargs_returned):
    args_values = dict(zip(ARGS, range(len(ARGS))))
    print('  | '+function.__name__ + ':', timeit(lambda: function(**args_values), number=1000))
