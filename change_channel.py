import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('bus.jpg')
b,g,r=cv2.split(img)

b=cv2.add(b,20)
img_modified=cv2.merge((b,g,r))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img_modified, cv2.COLOR_BGR2RGB))
plt.title('modified')
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('original')
plt.show()