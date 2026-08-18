import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A=np.array(A)
    n=A.shape[0]
    m=A.shape[1]
    result = np.zeros((m, n))
    for i in range(n):
        for j in range(m):
            result[j][i]=A[i][j]
    return result
