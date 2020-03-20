import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

plt.matplotlib.rc('text', usetex = True)
plt.matplotlib.rc('grid', linestyle = 'dotted')
plt.matplotlib.rc('figure', figsize = (6,5.5))

x = np.linspace(0, 2, 500)
c = np.sqrt(8*((3*1)-1))
d = np.sqrt(8*((3*5)-1))
e = np.sqrt(8*((3*10)-1))
f = 2*np.sqrt(x)*(np.sqrt((np.sqrt(8*(3*1-1)))))
g = 2*np.sqrt(x)*(np.sqrt((np.sqrt(8*(3*5-1)))))
h = 2*np.sqrt(x)*(np.sqrt((np.sqrt(8*(3*10-1)))))

plt.plot(x, (np.exp(-x*c))*f, label='$\lambda=1$')
plt.plot(x, (np.exp(-x*d))*g, label='$\lambda=5$')
plt.plot(x, (np.exp(-x*e))*h, label='$\lambda=10$')


plt.xlim((0, 2))
plt.ylim((0, 1))
plt.legend(bbox_to_anchor=(1,1), loc='upper left', fontsize=12)

plt.xlabel('$\eta$', fontsize=16)
plt.ylabel('$|\\varphi(\eta)|^2$', fontsize=16)
plt.grid(False)
plt.tight_layout(0.5)
plt.show()
