import sys
import cv2
import numpy as np
DELAY_BLUR = 500;

#Median Filter
from matplotlib import pyplot as plt
img = cv2.imread('SaltAndPepper_Input.png')

kernel = np.ones((2,3),np.float32)/6
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


#GaussianBlur
for i in xrange(1,31,2):
    gaussian_blur = cv2.GaussianBlur(img,(i,i),0)
    string = 'guassian_blur : kernel size - '+str(i)
    cv2.putText(gaussian_blur,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(123,123,123))
    cv2.imshow('Blur',gaussian_blur)
    cv2.waitKey(DELAY_BLUR)