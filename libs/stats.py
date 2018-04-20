def mean(X):
    soma = 0
    for i in X:
        soma = float(i) + soma
    return soma / float(len(X))

def stdev(X):
    soma = 0
    for i in X:
        soma = soma + ((i - mean(X)) ** 2)
    return (soma / float(len(X))) ** (1/2)

def var(Y):
    return (stdev(Y) ** 2)