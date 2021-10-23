import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y_1 = [0.09512, 0.10341, 0.04274, 0.05115, 0.13445, 0.03214, 0.13285, 0.06697, 0.11245, 0.03024, 0.10311]
y_2 = [0.00315, 0.00406, 0.00414, 0.00305, 0.00356, 0.00385, 0.00401, 0.00367, 0.00336, 0.00421, 0.00357]

plt.plot(x,y_1, label = 'using blockchain')
plt.plot(x, y_2, label ='without using blockchain')                
plt.ylabel('Time  taken (in sec)')
plt.legend()
plt.show()