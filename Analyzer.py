import numpy as np
import simoa.stats as stats
import scipy as sc
import Independence
import Uniform

alpha=.05

def readFile(filename):
    return np.loadtxt('./randomNumberFiles/'+filename)

def analyze(filename):
    print('#################################')
    print('analyzing file: ' + filename)
    # Read file
    data = readFile(filename + '.txt')

    # APPROX INDEPENDENCE
    # Run von nuemann
    stats.von_neumann_ratio_test(data, alpha, verbose=True)
    # run up and down
    Independence.upAndDownTest(data)
    # run above and below
    Independence.aboveAndBelowTest(data)

    # UNIFORM DISTRIBUTION
    # run chi squared
    Uniform.chiSquaredTest(data)

    # run kolmogorov smirnov
    kstestLess = sc.stats.kstest(data, sc.stats.uniform.cdf, alternative='less')
    kstestGreater = sc.stats.kstest(data, sc.stats.uniform.cdf, alternative='greater')
    print(kstestGreater, kstestLess)
    print(kstestLess[1] <=.05, kstestGreater[1]<=.05)



analyze('JsfRandom')
analyze('Pcg64dxsmRandom')
analyze('pythonBaseRandom')
analyze('Xoshiro256Random')

analyze('baserandom')