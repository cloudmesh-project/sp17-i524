#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:56:31 2017
I524 Project: OCR
Preprocessing
Binarization
@author: saber
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

image_path = 'sample1.png'
image_arr = cv2.imread(image_path, 0)

plt.figure(1)
plt.subplot(311)
# Plot histogram of data
plt.hist(image_arr.flatten())

hist, bin_centers = np.histogram(image_arr)

weight1 = np.cumsum(hist)
weight2 = np.cumsum(hist[::-1])[::-1]

mean1 = np.cumsum(hist * bin_centers[1:]) / weight1
mean2 = np.cumsum((hist * bin_centers[1:]) / weight2[::-1])[::-1]

variance12 = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:])**2

idx = np.argmax(variance12)
threshold = bin_centers[:-1][idx]

img_bin = np.zeros(image_arr.shape)
for i in range(image_arr.shape[0]):
    for j in range(image_arr.shape[1]):
        if image_arr[i, j] > threshold:
            img_bin[i, j] = 255
        else:
            img_bin[i, j] = 0
#plt.imshow(image_arr)
#plt.imshow(img_bin)


plt.subplot(312)
plt.imshow(image_arr, 'gray')
plt.subplot(313)
plt.imshow(img_bin, 'gray')
