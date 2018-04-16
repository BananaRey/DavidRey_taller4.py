import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys 


n_pixel_kernel=sys.argv[0]

color=plt.imread('imagen.png')
n_pixel_kernel=1.0
def fourier(M):
	a=M.shape[2]
	n_columnas=M.shape[1]
	n_filas=M.shape[0]
	N=np.zeros((n_filas,n_columnas,a), dtype=complex)
	for u in range(n_filas):
		for v in range(n_columnas):
			for x in range(n_filas):
				for y in range(n_columnas):
					for i in range(a):
  						N[u][v][i]+=(M[x][y][i]*np.exp((-2.0j*np.pi*(float(u)*float(x)/float(n_filas)+float(v)*float(y)/float(n_columnas)))))
	return(N)

def fourier_2(M):
	a=M.shape[2]
	n_filas=M.shape[1]
	n_columnas=M.shape[0]
	N=np.zeros((n_filas,n_columnas,a))
	for u in range(n_filas):
		for v in range(n_columnas):
			for x in range(n_filas):
				for y in range(n_columnas):
					for i in range(a):
						N[u][v][i]+=(M[x][y][i]*np.exp((2.0j*np.pi*(float(u)*float(x)/float(n_filas)+float(v)*float(y)/float(n_columnas)))))
	return(N)



def gausian_2D(shape,sigma=1.0):
	k=(1/(2*np.pi*(sigma**2.0)))
	N=np.zeros((shape[0],shape[1],shape[2]))
	for x in range(shape[0]):
		for y in range(shape[1]):
			for i in range(shape[2]):
				N[x][y][i]=k*np.exp((float(x**2)+float(y**2))/(-2.0*(sigma**2)))
	return(N)
	
a=fourier_2(fourier(color)*fourier(gausian_2D(color.shape,n_pixel_kernel)))
plt.imshow(a)
plt.savefig('n_pixel_kernel.png')



