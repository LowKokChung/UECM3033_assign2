import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as lg

img=mpimg.imread ('Handsome.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

#other picture
img2=mpimg.imread('Lenna.jpg')
[r2,g2,b2] = [img2[:,:,i] for i in range(3)]

red = {'Index' : 0,'Mat': r2, 'Color' : 'Reds'}
green = {'Index' : 1, 'Mat': g2, 'Color' : 'Greens'}
blue = {'Index' : 2, 'Mat': b2, 'Color' : 'Blues'}
rgb = [red,green,blue]

for color in rgb:
    plt.imshow(color['Mat'], cmap = color['Color'])
    plt.show()


# SVD decomposition of img
    U,s,V = lg.svd(color['Mat'])
    
    S = np.zeros(color['Mat'].shape,s.dtype)
    
    for i in range(s.size):
        S[i][i] = s[i]
        
    #check: Get back A
    #check = np.dot(np.dot(U,S),V)
    #plt.imshow(check, cmap ='Reds')
    #plt.show()
    color['U'] = U
    color['eigenval'] = s
    color['S'] = S
    color['V'] = V
    
img_new = np.zeros_like(img2)

for dimension in (30,200):
    for color in rgb:
        S_new = np.zeros(color['Mat'].shape,s.dtype)
        
        for i in range(dimension):
            S_new[i][i] = color['eigenval'][i]
            
        img_new[:,:,color['Index']]= np.dot(np.dot(color['U'],S_new),color['V'])
    plt.imshow(img_new)
    if (dimension == 30 ):
        plt.imsave('Lenna_lower.jpg',img_new)
    if (dimension == 200):
        plt.imsave('Lenna_better.jpg',img_new)
    plt.show()
