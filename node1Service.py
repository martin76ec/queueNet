from normal import extractNormal
from exponential import extractExponential

def node1Service(n_med_n1, n1, tsuc, t, tS1, nS1, departures1, service_2_lambda,
                    n_med_n2, n2, nLL2, arrivals2, tS2, 
                    n_med_n3, n3, nLL3, arrivals3, tS3):
    n_med_n1 += n1 * (tsuc - t)
    n1 -= 1
    nS1 += 1
    departures1.append(tsuc)
    U = extractNormal(0, 1)
    if U <= 0.4:
        n_med_n2 += n2 * (tsuc - t)
        n2 += 1
        nLL2 += 1
        arrivals2.append(tsuc)
        if n2 == 1:
            Z = extractExponential(service_2_lambda)
            tS2 = tsuc + Z
    else: 
        n_med_n3 += n3 * (tsuc - t)
        n3 += 1
        nLL3 = nLL3 + 1
        arrivals3.append(tsuc)
        if n3 == 1:
            W = extractNormal(7, 1)
            tS3 = tsuc + W 
    t = tsuc
    if n1 > 0:
        S = extractNormal(2, 0.5)
        tS1 = t + S
    return [n_med_n1, n1, nS1, departures1, 
                    n_med_n2, n2, nLL2, arrivals2, tS2, 
                    n_med_n3, n3, nLL3, arrivals3, tS3, tS1, t]