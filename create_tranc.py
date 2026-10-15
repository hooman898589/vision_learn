from typing import final

import numpy as np
import matplotlib.pyplot as plt
import cv2



img=cv2.imread("bus.jpg")

crroped_img = img.copy()
crroped_img = crroped_img[400:800 ,400:800]
crroped_img=cv2.add(crroped_img,20)

img=cv2.add(img,20)


z=np.zeros(img.shape[:2] ,dtype=np.uint8)

circle=cv2.circle(z,(600,600),200,(255,255,255),-1)

circle2=cv2.circle(z,(600,600),200,(255,255,255),-1)
circle2=cv2.bitwise_and(img,img,mask=circle2)


final_img=cv2.bitwise_and(img,img,mask=cv2.bitwise_not(circle))
final_img=cv2.cvtColor(final_img,cv2.COLOR_BGR2BGRA)
mask=np.any(final_img==0,axis=2)
final_img[mask]=[255,255,255,0]

final_img[np.logical_not(mask),3]=50
circle2=cv2.cvtColor(circle2,cv2.COLOR_BGR2BGRA)

mask=np.any(circle2==0,axis=2)
circle2[mask]=[255,255,255,0]
circle2[~mask,3]=255
cv2.imshow("img",final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("",circle2)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask=np.any(final_img[:,:,:3]==[255,255,255],axis=2)

final_img[mask]=circle2[mask]
cv2.imwrite("bus231.png",final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

