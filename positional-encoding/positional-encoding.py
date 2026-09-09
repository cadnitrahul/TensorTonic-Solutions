import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pos_enc=[]
    for pos in range(seq_len):
        rows = []

        for j in range(d_model):
            i = j // 2

            if j % 2 == 0:
                rows.append(
                    np.sin(pos / pow(base, (2 * i) / d_model))
                )
            else:
                rows.append(
                    np.cos(pos / pow(base, (2 * i) / d_model))
                )

        pos_enc.append(rows)
    return np.array(pos_enc)