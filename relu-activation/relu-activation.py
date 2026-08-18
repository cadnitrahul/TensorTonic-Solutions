import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    z=np.array(x)
    return np.maximum(0, z)
    pass