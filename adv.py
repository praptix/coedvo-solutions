import cv2

# Load the pre-trained Haar Cascade file for vehicle detection
# Make sure the XML file is in the same directory or provide the full path
cascade_src = 'haarcascade_car.xml'
vehicle_cascade = cv2.CascadeClassifier(cascade_src)

# Option 1: Detect vehicles in an image
def detect_vehicles_in_image(C:\Users\choud\Downloads\ibm.jpg):
    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the image
    vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw rectangles around detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the output image
    cv2.imshow('Vehicle Detection', img)

    # Wait for key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Option 2: Detect vehicles in a video
def detect_vehicles_in_video(C:\Users\choud\Downloads\Piyu bole _ Siya Guglani Choreography.mp4=None):
    # Capture video from file or webcam (if video_path is None, webcam will be used)
    if video_path:
        cap = cv2.VideoCapture(video_path)
    else:
        cap = cv2.VideoCapture(0)  # Default webcam

    while True:
        # Read frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles in the frame
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 1)

        # Draw rectangles around detected vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the output frame
        cv2.imshow('Vehicle Detection', frame)

        # Exit loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
# To detect vehicles in an image
detect_vehicles_in_image('car_image.jpg')  # Provide the path to your image

# To detect vehicles in a video
# detect_vehicles_in_video('traffic_video.mp4')  # Provide the path to your video or keep it None for webcam
