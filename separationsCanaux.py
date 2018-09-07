import cv2

img = cv2.imread('images/hexa.png')
blues = img[:, :, 0]
greens = img[:, :, 1]
reds = img[:, :, 2]

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600, 600)

cv2.namedWindow("greens", cv2.WINDOW_NORMAL)
cv2.resizeWindow('greens', 600, 600)

cv2.namedWindow("reds", cv2.WINDOW_NORMAL)
cv2.resizeWindow('reds', 600, 600)

# Saving an Image on a key press
cv2.imshow('image', blues)
cv2.imshow('greens', greens)
cv2.imshow('reds', reds)


print("press 's' to save the image as 'image_test_2.png\n")
key = cv2.waitKey(0) & 0xFF # NOTE: if you are using a 64-bit machine,this needs to be: key = cv2.waitKey(0) & 0xFF
if key == 27: # wait for the ESC key to exit
    cv2.destroyAllWindows()
elif key == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('image_test_2.png', img)
    cv2.destroyAllWindows()