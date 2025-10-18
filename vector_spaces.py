import numpy as np
import matplotlib.pyplot as plt

def is_linearly_independent(vectors):
    matrix = np.array(vectors).T 
    return np.linalg.matrix_rank(matrix) == len(vectors)

if __name__ == '__main__':
    vecs = [[1,0,0], [0,1,0], [0,0,1]]
    print(f'Independent: {is_linearly_independent(vecs)}')
    