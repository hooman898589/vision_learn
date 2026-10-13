import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('images.png')
b,g,r=cv2.split(img)



zeros=np.zeros_like(b,np.uint8)
blue_mode=cv2.merge([zeros,zeros,b])
green_mode=cv2.merge([zeros,g,zeros])
red_mode=cv2.merge([r,zeros,zeros])

plt.subplot(1,3,1)
plt.imshow(blue_mode)
plt.subplot(1,3,2)
plt.imshow(green_mode)
plt.subplot(1,3,3)
plt.imshow(red_mode)
plt.show()