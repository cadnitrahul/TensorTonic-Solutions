def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x=x0
    for _ in range(steps):
        # df=2*a*x+b
        # da=2*(x**2)
        # a=a-(lr*da)
        # b=b-(lr*x0)
        # c=c-lr
        df=2*a*x+b
        x=x-(lr*df)
    return x