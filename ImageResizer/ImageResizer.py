import cv2

# Get the image name from the user
image_name = input("Enter image name: ")

# Read the image using OpenCV
image = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not load the image.")
    exit()

# Display the original image
cv2.imshow('Original Image', image)

# Define the scale factor
scale = 50

# Calculate the new dimensions
new_width = int(image.shape[1] * scale / 100)
new_height = int(image.shape[0] * scale / 100)

# Resize the image
output = cv2.resize(image, (new_width, new_height))

# Display the resized image
cv2.imshow('Resized Image', output)

# Save the resized image
cv2.imwrite('newImage.jpg', output)

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()