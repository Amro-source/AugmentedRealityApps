import cv2

# Create a window to display the camera feed
cv2.namedWindow('Tangerine Tracker', cv2.WINDOW_NORMAL)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Set the camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Load the tangerine template
template = cv2.imread('tangerine_template.png')

# Define the tracking region of interest (ROI)
tracking_roi = None

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # If we haven't found the tangerine yet, search for it
    if tracking_roi is None:
        # Use template matching to find the tangerine
        result = cv2.matchTemplate(gray, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # If we found a match, define the tracking ROI
        if max_val > 0.8:
            tracking_roi = (max_loc[0], max_loc[1], template.shape[1], template.shape[0])

    # If we've found the tangerine, track it
    if tracking_roi is not None:
        # Extract the ROI from the frame
        roi = frame[tracking_roi[1]:tracking_roi[1]+tracking_roi[3], tracking_roi[0]:tracking_roi[0]+tracking_roi[2]]

        # Display the ROI
        cv2.imshow('Tangerine ROI', roi)

        # Draw a rectangle around the tracked tangerine
        cv2.rectangle(frame, (tracking_roi[0], tracking_roi[1]), (tracking_roi[0]+tracking_roi[2], tracking_roi[1]+tracking_roi[3]), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Tangerine Tracker', frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed, exit the loop
    if key == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
