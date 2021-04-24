import numpy as np
import math
import scipy.stats as stats

def countRuns(data):
    sequence = ""
    for i in range(1, data.size):
        if (data[i] > data[i-1]):
            sequence = sequence + '+'
        else:
            sequence = sequence + '-'
    previous = 'undefined'
    runs=1
    for sign in sequence:
        if (previous != 'undefined'):
            if (sign != previous):
                runs = runs + 1
        previous = sign
    return runs

def upAndDownTest(data, zscore=1.96):
    runs = countRuns(data)
    expectedRuns = (2*data.size) / 3
    variance = (16*data.size - 29) / 90
    z_naught = (runs - expectedRuns) / math.sqrt(variance)
    reject = abs(z_naught) > zscore
    print('Z score: {}'.format(z_naught))
    if (reject):
        print(" rejecting independence based on up/down test")
    else:
        print(" not rejecting independence based on up/down test")

def countAboveAndBelows(data):
    aboves = 0
    belows = 0
    mean = np.mean(data)
    sequence = ''
    for i in data:
        if (i>mean):
            sequence = sequence + '+'
            aboves = aboves + 1
        else:
            sequence = sequence + '-'
            belows = belows + 1
    previous = 'undefined'
    runs=1
    for sign in sequence:
        if (previous != 'undefined'):
            if (sign != previous):
                runs = runs + 1
        previous = sign
    return runs, aboves, belows

def aboveAndBelowTest(data, zscore=1.96):
    runs, aboves, belows = countAboveAndBelows(data)
    expectedRuns = ((2 * aboves * belows) / data.size) + .5
    variance_numerator = ((2 * aboves * belows) * (( 2 * aboves * belows ) - data.size))
    variance_denominator = ((data.size**2) * (data.size - 1))
    variance = variance_numerator / variance_denominator
    z_naught = (runs - expectedRuns) / math.sqrt(variance)
    reject = abs(z_naught) > zscore
    print('Z score: {}'.format(z_naught))
    if (reject):
        print(" rejecting independence based on above/below test")
    else:
        print(" not rejecting independence based on above/below test")