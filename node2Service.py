from exponential import extractExponential
from normal import extractNormal

def node2Service(n_med_n2, n2, nS2, departures2, tS2, tsuc, 
                    n_med_n3, n3, nLL3, arrivals3, tS3, t, service_2_lambda):
    n_med_n2 += n2 * (tsuc - t)
    n2 -= 1
    nS2 += 1
    departures2.append(tsuc)
    if n2 > 0:
        Y = extractExponential(service_2_lambda)
        tS2 = tsuc + Y
    n_med_n3 += n3 * (tsuc - t)
    n3 += 1
    nLL3 += 1
    arrivals3.append(tsuc)
    if n3 == 1: 
        W = extractNormal(7, 1)
        tS3 = tsuc + W 
    t = tsuc
    return [n_med_n2, n2, nS2, departures2, tS2,
                n_med_n3, n3, nLL3, arrivals3, tS3, t]