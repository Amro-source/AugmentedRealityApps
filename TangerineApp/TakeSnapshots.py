
import cv2

# Create a window to display the camera feed
cv2.namedWindow('Tangerine Capture', cv2.WINDOW_NORMAL)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Set the camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a counter for the image files
image_counter = 0

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Tangerine Capture', frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'c' key is pressed, capture an image
    if key == ord('c'):
        # Save the image to a file
        image_file = f'tangerine_{image_counter}.png'
        cv2.imwrite(image_file, frame)
        print(f'Image saved to {image_file}')

        # Increment the image counter
        image_counter += 1

    # If the 'q' key is pressed, exit the loop
    elif key == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
