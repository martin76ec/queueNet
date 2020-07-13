from exponential import extractExponential
from clientArrival import clientArrival
from node1Service import node1Service
from node2Service import node2Service
from node3Service import node3Service
import numpy as np
import pdb

def queueNet(T, client_lambda , service_1_lambda, service_2_lambda, service_3_lambda):
    M = float('inf')
    t = tsuc = Tp = 0
    tLL1 = tS1 = tS2 = tS3 = M
    nLL1 = nLL2 = nLL3 = nS1 = nS2 = nS3  = n1 = n2 = n3 = 0
    n_med_n1 = n_med_n2 = n_med_n3 = 0
    arrivals = [[], [], []]
    departures = [[], [], []]
    exp_extract = extractExponential(client_lambda)
    
    if exp_extract > T: 
        Tp = t_med_system = n_med_n1 = n_med_n2 = n_med_n3 = 0;
    else:
        [n_med_n1, n1, nLL1, arrivals[0], t, tLL1, tS1] = clientArrival(n_med_n1, n1, exp_extract, t, nLL1, arrivals[0], client_lambda, tLL1, tS1, T)
        while (tLL1 or tS1 or tS2 or tS3) != M:
            if min(tLL1, tS1, tS2, tS3) == tLL1:
                tsuc = tLL1 
                tLL1 = M
                [n_med_n1, n1, nLL1, arrivals[0], t, tLL1, tS1] = clientArrival(n_med_n1, n1, tsuc, t, nLL1, arrivals[0], client_lambda, tLL1, tS1, T)
            if min(tLL1, tS1, tS2, tS3) == tS1:
                tsuc = tS1
                tS1 = M
                [n_med_n1, n1, nS1, departures[0], 
                    n_med_n2, n2, nLL2, arrivals[1], tS2, 
                    n_med_n3, n3, nLL3, arrivals[2], tS3, tS1, t] = node1Service(n_med_n1, n1, tsuc, t, tS1, nS1, departures[0], service_2_lambda,
                                n_med_n2, n2, nLL2, arrivals[1], tS2,
                                n_med_n3, n3, nLL3, arrivals[2], tS3)
            if min(tLL1, tS1, tS2, tS3) == tS2:
                tsuc = tS2
                tS2 = M
                [n_med_n2, n2, nS2, departures[1], tS2,
                    n_med_n3, n3, nLL3, arrivals[2], tS3, t] = node2Service(n_med_n2, n2, nS2, departures[1], tS2, tsuc, 
                                                                                n_med_n3, n3, nLL3, arrivals[2], tS3, t, service_2_lambda)
            if min(tLL1, tS1, tS2, tS3) == tS3:
                tsuc = tS3
                tS3 = M
                [n_med_n3, n3, nS3, departures[2], tS3] = node3Service(n_med_n3, n3, tsuc, t, nS3, departures[2], tS3)    
        Tp = max(0, t - T)
        ind = 0
        cumulative1 = cumulative2 = cumulative3 = 0
        while ind < nLL1:
            pdb.set_trace()
            cumulative1 = cumulative1 + departures[0][ind] - arrivals[0][ind] 
            ind += 1
        ind = 0
        while ind < nLL2:
            cumulative2 = cumulative2 + departures[1][ind] - arrivals[1][ind]
            ind += 1
        ind = 0
        while ind < nLL3:
            cumulative3 = cumulative3 + departures[2][ind] - arrivals[2][ind]
            ind += 1
        t_med_system = (cumulative1 / nLL1) + (0.4 * cumulative2 / nLL2) + (cumulative3 / nLL3)
        n_med_n1 = n_med_n1 / t
        n_med_n2 = n_med_n2 / t
        n_med_n3 = n_med_n3 / t
    return [Tp, t_med_system, n_med_n1, n_med_n2, n_med_n3]
