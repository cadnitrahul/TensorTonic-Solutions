import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x=np.array(x)
    p=np.array(p)
    expecte_value=np.sum(x*p)
    if x.shape!=p.shape:
        raise ValueError("s and p msut have the same shape")
    if np.sum(p)!=1:
        raise ValueError("prob must sum to 1")
    return expecte_value
