import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

plt.matplotlib.rc('text', usetex = True)
plt.matplotlib.rc('grid', linestyle = 'dotted')
plt.matplotlib.rc('figure', figsize = (6,5.5))

x = np.linspace(0, 1.5, 500)
c = 1+(1/2)*(np.sqrt(1 + (-1)*(-1 - 2) - 4*((3*1 - 1)*(-1) + (1/2)*np.sqrt((3*1) - 1))))
d = 1+(1/2)*(np.sqrt(1 + (-1)*(-1 - 2) - 4*((3*5 - 1)*(-1) + (1/2)*np.sqrt((3*5) - 1))))
e = 1+(1/2)*(np.sqrt(1 + (-1)*(-1 - 2) - 4*((3*10 - 1)*(-1) + (1/2)*np.sqrt((3*10) - 1))))
plt.plot(x, (np.abs(x**(1+c)))**2, label='$\lambda=1$')
plt.plot(x, (np.abs(x**(1+d)))**2, label='$\lambda=5$')
plt.plot(x, (np.abs(x**(1+e)))**2, label='$\lambda=10$')

plt.xlim((0, 1.5))
plt.ylim((0, 0.5))
plt.legend(bbox_to_anchor=(1,1), loc='upper left', fontsize=12)

plt.xlabel('$a$', fontsize=16)
plt.ylabel('$|\psi(a)|^2$', fontsize=16)
plt.grid(False)
plt.tight_layout(0.5)
plt.show()
