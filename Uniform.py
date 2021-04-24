import numpy as np
import math
import matplotlib.pyplot as pyplot

def getFrequencies(data, k):
    bucketSize = 1/k
    frequencies = np.zeros(k)
    for i in data:
        bucket = math.floor(i / bucketSize)
        frequencies[bucket] = frequencies[bucket] + 1

    expectedFrequencies = np.full(k, data.size * bucketSize)
    return frequencies, expectedFrequencies

def chiSquaredTest(data, k=10, chiSquare=3.325):
    frequencies, expectedFrequencies = getFrequencies(data, k)
    
    pyplot.hist(data, bins=k, range=(0,1))
    pyplot.show()
    chiSqured_naught = 0
    for i in range(frequencies.size):
        j = ((frequencies[i] - expectedFrequencies[i]) ** 2)/expectedFrequencies[i]
        chiSqured_naught = chiSqured_naught + j
        
    reject = chiSqured_naught > chiSquare
    print('Chi Squared: {}'.format(chiSqured_naught))
    if (reject):
        print(" rejecting uniformity based on chi squared test")
    else:
        print(" not rejecting uniformity based on chi squared test")
    
