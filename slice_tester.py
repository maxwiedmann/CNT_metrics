from image_slicer import *
import cv2

img = cv2.imread('/slice_test/test_slice_image.jpg', cv2.IMREAD_GRAYSCALE)

slices = slice_image(img, "test_slice_image.jpg", size = 128, reslice = False)



#slices = slice_image(img, img_name = "None", size = 128, reslice = False)