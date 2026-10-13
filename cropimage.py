import cv2
import matplotlib.pyplot as plt

image=cv2.imread('bus.jpg')

highit, wight, _= image.shape
print(highit, wight)
crop=image[400:500,200:350]
crop=cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
plt.imshow(crop)
plt.show()

cv2.imwrite('human.jpg',cv2.cvtColor(crop, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()