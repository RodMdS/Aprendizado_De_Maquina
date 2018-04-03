import numpy as np

def split_train_test(n_elem, perc_train, seed):
    lista = [ i for i in range(n_elem) ]
    np.random.seed(seed)
    np.random.shuffle(lista)
    aux = n_elem * perc_train
    return lista[:int(aux)], lista[int(aux):]