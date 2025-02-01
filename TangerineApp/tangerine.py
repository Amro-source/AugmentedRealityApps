import cv2

# Load the template image (the tangerine)
template = cv2.imread('tangerine.png')

# Load the source image (the camera feed)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Convert the template to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # Use template matching to detect the tangerine
    result = cv2.matchTemplate(gray, template_gray, cv2.TM_CCOEFF_NORMED)
    
    # Find the maximum value in the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # If the maximum value is greater than 0.8, consider it a match
    if max_val > 0.8:
        # Draw a rectangle around the matched tangerine
        cv2.rectangle(frame, max_loc, (max_loc[0] + template.shape[1], max_loc[1] + template.shape[0]), (0, 255, 0), 2)
        
        # Display the virtual business card
        # TODO: implement virtual business card display
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
