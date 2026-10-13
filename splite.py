import cv2
import matplotlib.pyplot as plt

img=cv2.imread('images.png')
b,g,r=cv2.split(img)
plt.subplot(1,3,1)
plt.imshow(b,cmap='gray')
plt.title('blue')
plt.subplot(1,3,2)
plt.imshow(g,cmap='gray')
plt.title('green')
plt.subplot(1,3,3)
plt.imshow(r,cmap='gray')
plt.title('red')
plt.show()
