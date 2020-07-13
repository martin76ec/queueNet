import random
import math

def extractNormal(u, sigma):
    uniformExtract = random.uniform(0, 1)
    y = (math.sqrt(uniformExtract ** 0.135) - math.sqrt((1 - uniformExtract) ** 0.135)) / (0.1975)
    return u + sigma * y



