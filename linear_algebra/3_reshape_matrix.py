import torch

def reshape_matrix(a, new_shape) -> torch.Tensor:
    """
    Reshape a 2D matrix `a` to shape `new_shape` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a tensor of shape `new_shape`, or an empty tensor on mismatch.
    """
    #classic solution
    #1.check wether dimension of current matrix and reshape matrix is same or not
    #2.if same flattern the matrix
    #3.now populate the new matrix

    # dimension check
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return torch.tensor([])
    #convert to tensor and reshape
    a_t = torch.as_tensor(a, dtype=torch.float)
    reshaped=a_t.reshape(new_shape) # reshapes the matrix according the new_shape
    return reshaped