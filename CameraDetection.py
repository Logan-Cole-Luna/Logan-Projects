import cv2
import numpy as np

def detect_shapes(frame, min_area):
    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mask the frame to only select red colors
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Find the contours of the red objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        # Ignore contours that are too small
        if cv2.contourArea(contour) < min_area:
            continue

        # Determine the shape of the contour
        shape = "unknown"
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            shape = "square"
        elif len(approx) == 5:
            shape = "pentagon"
        elif len(approx) == 6:
            shape = "hexagon"
        elif len(approx) >= 7:
            shape = "circle"

        # Draw the contour and shape on the frame
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Find the center of the contour and draw a point
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)


# Define the minimum and maximum boundaries of the red color range in the HSV color space
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not access the camera.")
        break

    # Detect shapes in the frame
    detect_shapes(frame, 500)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Check for user input to stop the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
