cdef extern from "Python.h":
    void* PyMem_Malloc(size_t size)
    void PyMem_Free(void* ptr)

cdef int** create_matrix(int rows, int cols):
    cdef int** matrix = <int**>PyMem_Malloc(sizeof(int*) * rows)
    for i in range(rows):
        matrix[i] = <int*>PyMem_Malloc(sizeof(int) * cols)
    return matrix

def mul(a, b):
    cdef int rows_a = len(a)
    cdef int cols_a = len(a[0])
    cdef int rows_b = len(b)
    cdef int cols_b = len(b[0])

    cdef int i, j, k
    cdef int** result = create_matrix(rows_a, cols_b)

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = 0
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    cdef list result_list = []
    for i in range(rows_a):
        result_list.append([result[i][j] for j in range(cols_b)])

    cdef int** matrix = result
    for i in range(rows_a):
        PyMem_Free(matrix[i])
    PyMem_Free(matrix)

    return result_list
