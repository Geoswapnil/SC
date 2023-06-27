#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
freq = 2.0

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

line_sin, = ax.plot(x, np.sin(x * freq), 'b', label='sin(x)')
line_cos, = ax.plot(x, np.cos(x * freq), 'r', label='cos(x)')
ax.legend()

freq = st.slider('Frequency', 0.1, 5.0, freq, 0.1)

line_sin.set_ydata(np.sin(x * freq))
line_cos.set_ydata(np.cos(x * freq))

st.pyplot(fig)


# In[ ]:




