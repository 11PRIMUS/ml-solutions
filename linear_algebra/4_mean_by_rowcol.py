#4- calculate mean by row and col


import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
    """
    Calculate mean of a 2D matrix per row or per column using PyTorch.
    
    Args:
        matrix: Input data (list of lists, NumPy array, or torch.Tensor).
        mode (str): 'row' or 'column'.
    
    Returns:
        torch.Tensor: 1D tensor containing the means.
    """
    a_t = torch.as_tensor(matrix, dtype=torch.float)

    if a_t.ndim != 2:
        raise ValueError("input must be a 2D matrix.")

    if mode =='row':
        #mean across columns for each row
        return a_t.mean(dim=1)
    elif mode =='column':
        #mean across rows for each column
        return a_t.mean(dim=0)
    else:
        raise ValueError("Mode must be row or col")
