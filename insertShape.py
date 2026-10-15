import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('bus.jpg')
cropped=img[100:400,100:400]
z=np.zeros((300,300),dtype=np.uint8)
circle=cv2.ellipse(z,(150,150),(150,150),0,0,360,255,-1)

shape=cv2.bitwise_and(cropped,cropped,mask=cv2.bitwise_not(circle))
shape2=shape.copy()
shape2[circle==255]=[255,25,255]

cv2.imshow('img',shape2)
cv2.waitKey(0)
cv2.destroyAllWindows()