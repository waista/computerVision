# library imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

# load an image
img = cv2.imread('image_test.png')
# load an image as a single channel grayscale
img_single_channel = cv2.imread('images/dolphin.png', 0)
# print some details about the images
print('The shape of img without second arg is: {}'.format(img.shape))
print('The shape of img_single_channel is:{}'.format(img_single_channel.shape))


# Saving an Image on a key press
img = cv2.imread('image_test.png')
cv2.imshow('Option to Save image', img)
print("press 's' to save the image as 'image_test_2.png\n")
key = cv2.waitKey(0) # NOTE: if you are using a 64-bit machine,this needs to be: key = cv2.waitKey(0) & 0xFF
if key == 27: # wait for the ESC key to exit
    cv2.destroyAllWindows()
elif key == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('image_test_2.png', img)
    cv2.destroyAllWindows()