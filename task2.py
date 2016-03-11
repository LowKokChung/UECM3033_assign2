import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as lg


img2=mpimg.imread('Handsome.jpg')
[r2,g2,b2] = [img2[:,:,i] for i in range(3)]

red = {'Index' : 0,'Mat': r2, 'Color' : 'Reds'}
green = {'Index' : 1, 'Mat': g2, 'Color' : 'Greens'}
blue = {'Index' : 2, 'Mat': b2, 'Color' : 'Blues'}
rgb = [red,green,blue]

for layer in rgb:
    plt.imshow(layer['Mat'], cmap = layer['Color'])
    plt.show()

# SVD decomposition of img
    U,s,V = lg.svd(layer['Mat'])
    
    S = np.zeros(layer['Mat'].shape,s.dtype)
    
    for i in range(s.size):
        S[i][i] = s[i]
       
    layer['U'] = U
    layer['eigenval'] = s
    layer['S'] = S
    layer['V'] = V
    
img_new = np.zeros_like(img2)

dimension = 30
for layer in rgb:
    S_30 = np.zeros(layer['Mat'].shape,s.dtype)
    
    for i in range(dimension):
        S_30[i][i] = layer['eigenval'][i]
        
    img_new[:,:,layer['Index']]= np.dot(np.dot(layer['U'],S_30),layer['V'])
plt.imshow(img_new)
plt.imsave('Handsome_lower_resolution.jpg',img_new)
plt.show()

dimension = 200
for layer in rgb:
    S_200 = np.zeros(layer['Mat'].shape,s.dtype)
    
    for i in range(dimension):
        S_200[i][i] = layer['eigenval'][i]
        
    img_new[:,:,layer['Index']]= np.dot(np.dot(layer['U'],S_200),layer['V'])
plt.imshow(img_new)
plt.imsave('Handsome_better_resolution.jpg',img_new)
plt.show()
