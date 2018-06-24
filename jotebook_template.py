
# coding: utf-8

# # Qutip imports

# In[7]:


from qutip.operators import sigmax, sigmay, sigmaz, identity
# position,  num
from qutip.tensor import tensor
from qutip.qip.gates import swap


# ## Numpy imports

# In[3]:


from numpy import sin, cos, tan, real, imag,  log
from numpy import array, append, linspace, arange
from numpy import add
from numpy.random import random, random_sample
from numpy import concatenate
# from numpy import pi


# ## Scipy imports

# In[4]:


from scipy.integrate import ode, odeint, complex_ode
from scipy.optimize import minimize


# ## Matplotlib imports

# In[ ]:


from matplotlib.pyplot import plot, figure, show, savefig
from matplotlib.pyplot import xlabel, ylabel, title, legend
from matplolib import rcParams


# ## Math imports

# In[6]:


from math import pi


# ## Cmath imports

# ## Date and datetime imports

# In[5]:


from datetime import date
from datetime import datetime# now


# ## Sympy imports

# In[8]:


from sympy import Function, dsolve, Eq, Derivative, symbols
# x, y, z, t = symbols('x y z t')
# k, m, n = symbols('k m n', integer=True)
# f, g, h = symbols('f g h', cls=Function)


# ## Miscellaneous imports

# Basic plotting commands

# In[ ]:


time_stuff = linspace(0, 4*pi, 1000)
p = tan(-2*time_stuff)
m = tan(-2*time_stuff)*((1 + cos(-4*time_stuff))/2)
t = -2*log(cos(-2*time_stuff))
figure()
plot(time_stuff, p, color='b', linestyle='--', label=r'$\mu_{+,real}$' );
plot(time_stuff, m, color='c', linestyle='-', label=r'$\mu_{-, rea;}$' );
plot(time_stuff, t, color='red', linestyle='--', label=r'$\mu_{3, imaginary}$' )
# plot(time_stuff, mmi, color='m', linestyle='-', label=r'$\mu_{-, imaginary}$' )

# plot(time_stuff, m3r, color='y', linestyle='--', label=r'$\mu_{3,real}$' )
# plot(time_stuff, m3i, color='green', linestyle='-', label=r'$\mu_{3, imaginary}$')

xlabel('time')
ylabel(r'$\mu$')
title(r'Plot of $\mu$ versus time')
legend()
savefig('Plot_of_mu_versus_time.png')  # saves  a blank file if saved after show()
show()

