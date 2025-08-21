#1- matrix vector dot product 
# Input:
# a = [[1, 2], [2, 4]], b = [1, 2]
# Output:
# [5, 10]

def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    if not a or not b: # check the value in matrix and vector , if none then return -1
        return -1
    cols = len(a[0]) #gets the length of columns
    if any(len(row) != cols for row in a): # same length of row and column
        return -1
    if cols != len(b): # no of cols must be equal to vector
        return -1
    return [sum(x * y for x, y in zip(row, b)) for row in a]
