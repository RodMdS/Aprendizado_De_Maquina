from Libs import stats as st
import numpy as np

class SimpleLinearRegression(object):
    b1 = None
    b0 = None
    
    def __init__(self):
        b1 = 0
        b0 = 0
    
    def fit(self, X, y):
        self.__class__.b1 = np.sum((X - st.mean(X)) * (y - st.mean(y))) / np.sum((X - st.mean(X)) ** 2)
        self.__class__.b0 = st.mean(y) - (self.b1 * st.mean(X))
    
    def predict(self, X):
        return self.__class__.b1 * X + self.__class__.b0
