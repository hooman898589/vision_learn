import cv2
import matplotlib.pyplot as plt

img=cv2.imread('bus.jpg')
new_image=img[:,:,0]*0.299  + img[:,:,1] * 0.587  + img[:,:,2]*  0.114

plt.imshow(new_image, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()