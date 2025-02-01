import cv2
import numpy as np

# Load the image
image = cv2.imread('image.png')

# Load the QR code image
qr_code_image = cv2.imread('qr_code.png')

# Convert the images to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
qr_code_gray = cv2.cvtColor(qr_code_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the images
_, image_thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
_, qr_code_thresh = cv2.threshold(qr_code_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Use template matching to find the QR code in the image
result = cv2.matchTemplate(image_thresh, qr_code_thresh, cv2.TM_SQDIFF)

# Find the minimum value in the result
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# If the minimum value is less than 0.5, consider it a match
if min_val < 0.5:
    # Draw a rectangle around the matched QR code
    cv2.rectangle(image, min_loc, (min_loc[0] + qr_code_thresh.shape[1], min_loc[1] + qr_code_thresh.shape[0]), (0, 255, 0), 2)

    # Save the output image
    cv2.imwrite('output.png', image)

    print("QR code found and highlighted in the output image.")
else:
    print("QR code not found in the image.")
