import cv2
from pyzbar import pyzbar

# Load the image
image = cv2.imread('image.png')

# Find QR codes in the image
qr_codes = pyzbar.decode(image)

# If QR codes are found, draw a rectangle around them and extract the data
if qr_codes:
    for qr_code in qr_codes:
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract and print the data stored in the QR code
        qr_code_data = qr_code.data.decode("utf-8")
        print("QR code data:", qr_code_data)

        # Augmented Reality part: display a virtual object on top of the QR code
        # For simplicity, let's display a red square
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), -1)

    # Display the output image
    cv2.imshow('Augmented Reality', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("QR code not found in the image.")
