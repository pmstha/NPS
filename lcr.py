#!/usr/bin/env python
# coding: utf-8

# # LCR in series

# ![img](lcr.png)

# Resonating frequency
# \begin{equation}
# f_0=\frac{1}{2\pi\sqrt{LC}}
# \end{equation}

# Quality factor
# \begin{equation}
# Q=\frac{1}{R}\sqrt{\frac{L}{C}}
# \end{equation}

# Inductive reactance
# \begin{equation}
# X_L=2\pi fL
# \end{equation}

# Capacitive reactance
# \begin{equation}
# X_C=\frac{1}{2\pi fC}
# \end{equation}

# Impedance
# \begin{equation}
# z=\sqrt{(X_L-X_C)^2+R^2}
# \end{equation}

# Current
# \begin{equation}
# I=\frac{V}{z}
# \end{equation}

# Phase angle
# \begin{equation}
# \phi=\tan^{-1}(\frac{X_L-X_C}{R})
# \end{equation}

# Power consumed
# \begin{equation}
# P=VI\cos\phi
# \end{equation}

# P.d. across L
# \begin{equation}
# V_L=IX_L
# \end{equation}

# P.d. across C
# \begin{equation}
# V_C=IX_C
# \end{equation}

# P.d. across R
# \begin{equation}
# V_R=IX_R
# \end{equation}

# P.d. across LC
# \begin{equation}
# V_{LC}=I(X_L -X_C)
# \end{equation}

# In[1]:


import numpy as np


# In[2]:


def fo(L,C):
    fr=2*np.pi*np.sqrt(L*C)
    fr=1/fr
    return fr


# In[3]:


def Q(L,C,R):
    ql=np.sqrt(L/C)/R
    return ql


# In[4]:


def inductiveReactance(L,f):
    XL=2*np.pi*L*f
    return XL


# In[5]:


def capacitiveReactance(C,f):
    XC=1/(2*np.pi*C*f)
    return XC


# In[6]:


def impedance(L,C,R,f):
    if(C==0):
        imp=np.sqrt((inductiveReactance(f,L))**2+R**2)
    else:
        imp=np.sqrt((inductiveReactance(f,L)-capacitiveReactance(f,C))**2+R**2)
    return imp


# In[7]:


def phase(L,C,R,f):
    if(C==0):
        pi=np.arctan(inductiveReactance(f,L)/R)*180/np.pi
    else:
        pi=np.arctan((inductiveReactance(f,L)-capacitiveReactance(f,C))/R)*180/np.pi
    return pi


# In[8]:


def power(L,C,R,f,v):
    ph=phase(L,C,R,f)
    cur=v*(impedance(L,C,R,f))**(-1)
    p=v*cur*np.cos(np.pi*ph/180)
    return p


# In[ ]:




