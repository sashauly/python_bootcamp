import timeit

setup_code = """
x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
y = [[1,2],[1,2],[3,4]]
"""

python_code = """
from matrix.multiply import mul

mul(x, y)
"""

cython_code = """
from matrix.multiply import mul
mul(x, y)
"""

python_time = timeit.timeit(python_code, setup=setup_code, number=10000)
cython_time = timeit.timeit(cython_code, setup=setup_code, number=10000)

print(f"Pure Python time: {python_time}")
print(f"Cython time: {cython_time}")
