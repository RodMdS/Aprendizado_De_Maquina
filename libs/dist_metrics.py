import numpy as np

def minkowski_distance(X, row, p):
    X_ = (X - row) ** p
    return np.sum(X_, axis=1) ** (1 / p)

def euclidean_distance(X, row): # Dica: usar minkowski_distance com p=2.
    return minkowski_distance(X, row, 2)

def manhattan_distance(X, row): # Dica: usar minkowski_distance com p=1.
    return minkowski_distance(X, row, 1)

def chebyshev_distance(X, row):
    return np.max(X - row)