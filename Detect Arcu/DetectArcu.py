import cv2
import numpy as np

# Define the marker
marker_image = cv2.imread('marker.png')

# Define the virtual cube
cube_image = cv2.imread('cube.png')

# Define the video file
video_file = 'video.mp4'

# Define the threshold for marker detection
threshold = 0.5

# Initialize the video capture
cap = cv2.VideoCapture(video_file)

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

while True:
    # Read a frame from the video file
    ret, frame = cap.read()

    # If the frame is not read, break the loop
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the marker
    marker_corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict)
    print(marker_corners)
    
    # If markers are detected
    if marker_corners:
        # Iterate over the detected markers
        for i, corner in enumerate(marker_corners):
            # Check if the corner list is not empty
            if len(corner) > 0:
                # Draw a bounding box around the marker
                #cv2.drawContours(frame, [corner], -1, (0, 255, 0), 2)

                # Get the homography matrix
                homography_matrix, _ = cv2.findHomography(corner, np.array([[0, 0], [marker_image.shape[1], 0], [marker_image.shape[1], marker_image.shape[0]], [0, marker_image.shape[0]]]))

                # Warp the cube image to the marker
                warped_cube = cv2.warpPerspective(cube_image, homography_matrix, (frame.shape[1], frame.shape[0]))

                # Overlay the warped cube on the frame
                frame = cv2.addWeighted(frame, 1, warped_cube, 0.5, 0)

    # Display the frame
    cv2.imshow('Augmented Reality', frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
