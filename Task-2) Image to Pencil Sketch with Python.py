# Description: This program converts an image to a pencil sketch

# pip install opencv-python

# Import the library
import cv2

# Get the image location and the image file name
img_location = 'D:/'
filename = 'scenary.png'

# Read in the image
img = cv2.imread(img_location+filename)

#Convert the image to gray color
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
inverted_gray_img = 255 - gray_image

#Blur the image by gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21,21), 0)

#Invert the blur image
inverted_blur_img = 255 - blurred_img

#Create the pencil sketch image
pencil_sketch_img = cv2.divide(gray_image,inverted_blur_img, scale=256.0)

# Show the image
cv2.imshow('Original Image', img)
cv2.imshow('Gray_Color Image', gray_image)
cv2.imshow('Inverted Image', inverted_gray_img)
cv2.imshow('Blurred Image', blurred_img)
cv2.imshow('Inverted Blurred Image', inverted_blur_img)
cv2.imshow('Pencil Sketch Image', pencil_sketch_img)
cv2.waitKey(0)















