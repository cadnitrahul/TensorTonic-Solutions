import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    # print(X[0][0],X[1][0])
    n = X.shape[0]
    w = np.zeros(X.shape[1])
    # print(w)
    b = 0
    for _ in range(steps):
        z=X@w+b
        p=_sigmoid(z)
        loss=-np.mean(y*np.log(p)+(1-y)*np.log(1-p))
        # compute the gradient
        dw=(X.T@(p-y))/n
        dl=np.mean(p-y)
        w=w-lr*dw
        b=b-lr*dl
    return w,b