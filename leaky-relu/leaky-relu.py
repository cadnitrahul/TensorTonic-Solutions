import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    y=np.array(x)
    result = np.where(y >= 0, y, alpha * y)
    return result
    # pass