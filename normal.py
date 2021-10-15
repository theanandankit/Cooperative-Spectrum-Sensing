import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from numpy import sqrt
from scipy import special as sp

def inv(value):
    return sqrt(2)*sp.erfinv(1 - 2*value)

gain = np.arange(0, 5, 0.25)
Mean = 0
SD = 1
noice = scipy.stats.norm.pdf(gain,Mean,SD)
plt.plot(gain, noice)
plt.show()

No_of_sample = noice.size

a = 0
x_mean = 0

for x in gain:
    x_mean += (noice[a] * ( 1 + (gain[a]**2)))
    a = a + 1

a = 0

x_variance = 0
for x in gain:
    x_variance += (noice[a]**2) * (1 + 2*(gain[a]**2))
    a = a + 1

x_variance = x_variance/gain.size

qf = np.linspace(0,1,100)

thres = []

for temp in qf:
    thres.append((inv(1 - temp)*x_variance) + x_mean)

no_x_mean = 0

for x in noice:
    no_x_mean += x

no_x_variance = 0

for x in noice:
    no_x_variance += x**2

no_x_variance = no_x_variance/noice.size

no_thres = []

for temp in qf:
    no_thres.append((inv(1 - temp)*no_x_variance) + no_x_mean)

plt.plot(qf,thres, label = 'with primary user')
plt.plot(qf, no_thres, label ='without primary user')
plt.xlabel('Probability of False Alarm')                
plt.ylabel('Threshold')
plt.legend()
plt.show()