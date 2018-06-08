import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

ksize = 100

img = cv2.imread('Apple-iMac-and-MacBook-Retina-Display-Wallpaper-5K-Apple-Logo-Design-5120x2880.jpg')

kernel = np.asarray([
    [1,2,3,2,1],
    [2,3,4,3,2],
    [3,4,5,4,3],
    [2,3,4,3,2],
    [1,2,3,2,1]
])/np.sum([
    [1,2,3,2,1],
    [2,3,4,3,2],
    [3,4,5,4,3],
    [2,3,4,3,2],
    [1,2,3,2,1]
])
print(kernel)
dst = cv2.filter2D(img,-1,kernel)

for i in range(1000):
    dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.imwrite("out.png",dst)