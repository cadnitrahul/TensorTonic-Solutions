import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    n=A.shape[0]
    m=A.shape[1]
    sum=0
    for i in range(n):
        for j in range(m):
            if i==j:
                sum+=A[i][i]
            else: 
                continue
    return sum
