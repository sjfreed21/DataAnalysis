import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
wdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 3/'
img = mpimg.imread(wdir+'alps.png')

plt.close('all')
plt.figure()
# plt.imshow(img)

# f2=plt.figure('Statistics Blue',figsize=[10,5])
# plt.hist(img[:,:,2].flatten())
# plt.show()

fig=plt.figure()
red=img[:,:,0]
grn=img[:,:,1]
blu=img[:,:,2]
print('image.shape',img.shape)

th = 0.75
cld = np.where((red > th) & (grn > th) & (blu > th))
'''
tra     =np.ones([img.shape[0],img.shape[1]])
tra[cld]=0
img=np.stack([red,grn,blu,tra],axis=2)
'''
red[cld]=1
grn[cld]=1
blu[cld]=1
img=np.stack([red,grn,blu],axis=2)


plt.imshow(img)
plt.title("Th = " + str(th))
# mpimg.imsave(wdir+'dat/alps_m.png',img)

