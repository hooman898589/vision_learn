import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('bus.jpg')
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_modified=cv2.merge((hsv_img[:,:,0],cv2.add(hsv_img[:,:,1],20),cv2.add(hsv_img[:,:,2],20)))
img_modified=cv2.cvtColor(img_modified,cv2.COLOR_HSV2RGB)
plt.subplot(1,2,1)
plt.imshow(img_modified)
plt.title('modified')
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title('original')
plt.show()