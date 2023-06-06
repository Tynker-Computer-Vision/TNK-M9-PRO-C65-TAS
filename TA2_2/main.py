# Importing Library
import numpy as np
import cv2

# Define the input and output paths
inputPath = 'static/lion.png'

# Load the color image
originalImage = cv2.imread(inputPath)


# ------------Convert image to Grayscale --------------

# Convert the color image to grayscale image
grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# Save the color image to disk
outputPath = 'converted/grayScale.png'
cv2.imwrite(outputPath, grayscaleImage)

# Display the converted image
cv2.imshow('Grayscale Image', grayscaleImage)
cv2.waitKey(0)


# Display a message indicating that the image has been saved
print('Converted Grayscale image saved to disk : ' + outputPath)
