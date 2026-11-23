import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    arr = np.array(v)
    n = len(arr)

    mat = np.zeros((n,n), dtype=arr.dtype) 
    """
        Passing dtype=arr.dtype ensures that if v has floats like [1.5], the grid holds floats (1.5, 0.0) rather than  truncating them to integers (1, 0).
    """

    idx = np.arange(n)
    mat[idx, idx] = arr
        
    return mat