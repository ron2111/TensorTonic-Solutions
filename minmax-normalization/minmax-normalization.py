import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    arr = np.asarray(X, dtype=np.float64)
    x_min = np.min(arr, axis=axis, keepdims=True)
    x_max = np.max(arr, axis=axis, keepdims=True)
    data_range = x_max - x_min
    
    valid = data_range > eps
    safe_range = np.where(valid, data_range, 1.0)
    scaled = (arr - x_min) / safe_range
    return np.where(valid, scaled, 0.0)