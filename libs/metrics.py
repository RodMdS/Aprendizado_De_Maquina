import numpy as np

def mse(y_true, y_pred):
    soma = 0
    for i in range(0, len(y_pred)):
        soma = soma + ((y_true[i] - y_pred[i]) ** 2)
    return (soma / len(y_pred))

def rmse(y_true, y_pred):
    return mse(y_true, y_pred) ** (1/2)

def mae(y_true, y_pred):
    soma = 0
    for i in range(0, len(y_pred)):
        soma = soma + np.abs(y_true[i] - y_pred[i])
    return (soma / len(y_pred))