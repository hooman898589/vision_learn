import cv2
import matplotlib.pyplot as plt
img=cv2.imread('bus.jpg')
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rgb_img[200:400, 200:300]=(200,5,24)
plt.imshow(rgb_img)
plt.show()
cv2.imwrite('bus2.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()