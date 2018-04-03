import numpy as np

def standarlize(X):
    return (X - np.mean(X)) / np.std(X)

def normalize(X):
    return (X - np.min(X)) / (np.max(X) - np.min(X))