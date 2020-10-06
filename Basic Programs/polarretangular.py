# -*- coding: utf-8 -*-
"""polarRetangular.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jufhLacc0hYWmaGo6Y-Kimio0OnRvCly
"""

import numpy as np

def polarRetangular(Z, theta):
  theta = theta * (np.pi/180)

  polar_x = Z*np.cos(theta)
  polar_y = Z*np.sin(theta)

  r = complex(polar_x, polar_y)
  print(r)

Z = float(input('Entre com o valor polar: '))
theta = float(input('Entre com o valor do angulo em GRAUS: '))

polarRetangular(Z, theta)

