import numpy as np
import matplotlib.pyplot as plt
import cv2
png = cv2.imread('transparency.png',cv2.IMREAD_UNCHANGED)

cv2.imshow('img',png[:,:,:-1])
cv2.imshow("imag2",png[:,:,3])

cv2.waitKey(0)
cv2.destroyAllWindows()