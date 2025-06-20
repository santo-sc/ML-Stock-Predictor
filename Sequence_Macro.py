import numpy as np
def sequence(data, seq_length):
    X, y = [], []
    for i in range(seq_length, len(data)):
        X.append(data[i-seq_length:i, :]) 
        y.append(data[i, 0])  

    return np.array(X), np.array(y)