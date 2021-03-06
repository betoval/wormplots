import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

plt.matplotlib.rc('text', usetex = True)
plt.matplotlib.rc('grid', linestyle = 'dotted')
plt.matplotlib.rc('figure', figsize = (6,5.5))

x = np.linspace(0.95, 2, 500)
c = np.sqrt(2*((3*1)-1))
d = np.sqrt(2*((3*5)-1))
e = np.sqrt(2*((3*10)-1))
f = 2*x*(np.sqrt((np.sqrt(2*(3*1-1)))))
g = 2*x*(np.sqrt((np.sqrt(2*(3*5-1)))))
h = 2*x*(np.sqrt((np.sqrt(2*(3*10-1)))))

plt.plot(x, (np.exp(-(x**2)*c))*f, label='$\lambda=1$')
plt.plot(x, (np.exp(-(x**2)*d))*g, label='$\lambda=5$')
plt.plot(x, (np.exp(-(x**2)*e))*h, label='$\lambda=10$')


plt.xlim((0.95, 2))
plt.ylim((0, 0.5))
plt.legend(bbox_to_anchor=(1,1), loc='upper left', fontsize=12)

plt.xlabel('$a$', fontsize=16)
plt.ylabel('$|\psi(a)|^2$', fontsize=16)
plt.grid(False)
plt.tight_layout(0.5)
plt.show()