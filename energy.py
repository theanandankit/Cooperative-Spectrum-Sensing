import numpy as np
from numpy import sqrt
from scipy import special as sp
import statistics
import matplotlib.pyplot as plt

def inv(value):
    return sqrt(2)*sp.erfinv(1 - 2*value)

f = np.linspace(0,1,101)

variance = sqrt(statistics.variance(f))
mean = statistics.mean(f)

y = []

for x in f:
    y.append((inv(1 - x)*variance) + mean)

plt.plot(f,y)
plt.xlabel('Probability of False Alarm')                
plt.ylabel('Threshold')
plt.show()

# temp = 0
# for x in f:
#     temp = temp + x*x
# temp = temp / len(f)

# for x in f:
