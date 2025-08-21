#2 transpose of a matrix(2)
# input:
# a = [[1,2,3],[4,5,6]]
# Output:
# [[1,4],[2,5],[3,6]]

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    
    b = [list(row) for row in zip(*a)]
    return b

# a=[[1,2,3],[4,5,6]]
# *a unpacks the list  [1,2,3],[4,5,6]
# zip(*a) pair elements col Wise  [(1,4), (2,5), (3,6)]
# convert tuple into list

