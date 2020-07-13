import random
import math

def extractExponential(a):
        uniformExtract = random.uniform(0, 1)
        F = -math.log(1 - uniformExtract) / (a)
        return F

