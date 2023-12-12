import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure#(figsize=(25,5))
Z = np.random.rand(50, 50)
arr = np.array([[9,8,7,6,5,4,3, 2, 1],[1, 2, 3,4,5,6,7,8,9], [9,8,7,6,5,4,3, 2, 1]])
ar1 = np.array([[1,1,1,1,1,1,1,1,1],[3,3,3,3,3,3,3,3,3],[1,1,1,1,1,1,1,1,1]])
ar2 = np.array([[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2]])
ar3 = np.array([[1,2,1,1,1,1,2,1,2]])
#plt.subplot(4, 1, 1)
plt.pcolor(ar3, linewidths=0,cmap="Spectral")


plt.show()