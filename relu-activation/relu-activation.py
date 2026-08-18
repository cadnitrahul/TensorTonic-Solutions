import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    z=np.array(x)
    y=z*(z>0)
    return y
    pass