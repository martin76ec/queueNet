from normal import extractNormal

def node3Service(n_med_n3, n3, tsuc, t, nS3, departures3, tS3):
    n_med_n3 += n3 * (tsuc - t)
    n3 -= 1
    nS3 += 1 
    departures3.append(tsuc)
    R = 0
    if n3 > 0:
        if n3 < 5:
            R = extractNormal(7, 1)
        else:
            R = extractNormal(5, 1)
        tS3 = tsuc + R
    return [n_med_n3, n3, nS3, departures3, tS3]