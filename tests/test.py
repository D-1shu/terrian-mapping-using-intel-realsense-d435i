import numpy as np
import cv2

# Create a 640x480 black image
img = np.zeros((480, 640, 3), np.uint8)

# Define the grid dimensions
grid_size = 40
grid_rows = grid_size
grid_cols = grid_size

# Calculate the pixel spacing for the grid
grid_step_x = int((img.shape[1] - 100) / grid_cols)
grid_step_y = int((img.shape[0] - 100) / grid_rows)

# Calculate the center point of the grid
center_x = int(img.shape[1] / 2)
center_y = int(img.shape[0] / 2)

# Create an empty array to store the pixel tuples
pixels = np.zeros((grid_rows * grid_cols, 3), np.uint8)

# Create an empty list to store the pixel coordinates
pixel_coordinates = []

# Populate the arrays with equidistant pixel tuples and their coordinates
for i in range(grid_rows):
    for j in range(grid_cols):
        # Calculate the coordinates of the current pixel
        x = center_x + (j - grid_cols // 2) * grid_step_x
        y = center_y + (i - grid_rows // 2) * grid_step_y
        
        # Set the current pixel to red
        #pixels[i * grid_cols + j] = [0, 0, 255]
        
        # Append the current pixel coordinates as a tuple to the list
        pixel_coordinates.append((x, y))
        
        # Draw a circle at the current pixel
        cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

# Display the image
print(pixel_coordinates)
cv2.imshow("Grid of Pixels", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


