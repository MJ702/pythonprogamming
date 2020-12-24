import numpy as np

x = [5, 10, 15, 20, 25, 30, 35, 40]
f = [7, 11, 10, 9, 13, 11, 7, 3]

xsqrt = [i * i for i in x]
fxsqet = [i * j for i, j in zip(xsqrt, f)]
print(fxsqet)
fx = [i*j for i,j in zip(x, f)]
print(fx)
print(np.sum(f))
print(np.sum(fxsqet))
print(np.sum(fx))