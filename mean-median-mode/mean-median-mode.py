import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x=np.array(x)
    n=len(x)
    mean=np.sum(x)/n
    # median=0
    # print(x[n/2])
    median=np.median(x)
    counts = Counter(x)
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    mode = float(min(modes))

    return mean,median,mode