import cv2

# Load the pre-trained Haar Cascade classifier for vehicles
vehicle_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# Function to detect vehicles in an image
def detect_vehicles_in_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect vehicles using the Haar Cascade
    vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around the detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the output image
    cv2.imshow('Detected Vehicles', img)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to detect vehicles in a video
def detect_vehicles_in_video(video_path):
    # Open the video file or capture device
    cap = cv2.VideoCapture(video_path)

    # Loop over the frames
    while cap.isOpened():
        # Read the current frame
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles in the current frame
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around the detected vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the output frame
        cv2.imshow('Detected Vehicles', frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Optionally, save the video with detected vehicles
def save_detected_vehicles_video(input_video_path, output_video_path):
    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties (width, height, frames per second)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles in the frame
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around the detected vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Write the frame with the detected vehicles
        out.write(frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()

    print(f"Video saved as {output_video_path}")

# Example usage:
# For detecting vehicles in an image
detect_vehicles_in_image('vehicle_image.jpg')

# For detecting vehicles in a video
detect_vehicles_in_video('traffic_video.mp4')

# To save a video with detected vehicles (optional)
# save_detected_vehicles_video('traffic_video.mp4', 'output_detected_vehicles.avi')
