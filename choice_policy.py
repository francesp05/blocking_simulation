import numpy as np

def softmax(choices, tau):
    beta = 1 / tau  # exploration parameter
    vector = np.array(choices)
    exp = np.exp((beta)*(vector))
    probability = exp/np.sum(exp)
    return probability