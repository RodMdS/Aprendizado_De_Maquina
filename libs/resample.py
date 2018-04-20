import numpy as np

# n_elem - número total de elementos.
# n_split - número de folds. Mínimo: 2.
# shuffle - aleatoriza a ordem dos dados (True) ou não (False).
# seed - determina uma semente para geração de números aleatórios ou não (None).

# Retorno: 2 arrays (idx_train e idx_test), cada um com n_splits elementos: 
 # Exemplo para n_splits=3, teremos idx_train[0], idx_train[1] e idx_train[2].
 # Exemplo para n_splits=3, teremos idx_test[0], idx_test[1] e idx_test[2].

idx_train = []
idx_test = []

def split_k_fold(n_elem, n_splits=2, shuffle=True, seed=0):
    lista = [ i for i in range(n_elem) ]
    if shuffle == True:
        if seed != None:
            np.random.seed(seed)
        np.random.shuffle(lista)
    
    aux = n_elem / n_splits
    for i in range(n_splits):
        # print(i, lista)
        idx_test.append(lista[:int(aux)])
        idx_train.append(lista[int(aux):])
        lista = lista[int(aux):] + lista[:int(aux)]
    
    return idx_train, idx_test

def split_train_test(n_elem, perc_train, seed):
    lista = [ i for i in range(n_elem) ]
    np.random.seed(seed)
    np.random.shuffle(lista)
    aux = n_elem * perc_train
    return lista[:int(aux)], lista[int(aux):]
