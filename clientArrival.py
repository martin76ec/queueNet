from exponential import extractExponential
from normal import extractNormal
import numpy as np

def clientArrival(n_med_n1, n1, tsuc, t, nLL1, arrivals1, client_lambda, tLL1, tS1, T):
    n_med_n1 += n1 * (tsuc - t)
    n1 += 1 
    nLL1 += 1
    arrivals1.append(tsuc)
    t = tsuc
    Y = extractExponential(client_lambda)
    if t + Y < T: 
        tLL1 = t + Y
    if  n1 == 1:
        Y = extractNormal(2, 0.5)
        tS1 = t + Y
    return [n_med_n1, n1, nLL1, arrivals1, t, tLL1, tS1]