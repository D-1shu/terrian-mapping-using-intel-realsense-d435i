import numpy as np
import cv2

class GridOfPixels:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
    
    def create(self):
        # Create a black image
        img = np.zeros((self.height, self.width, 3), np.uint8)

        # Define the grid dimensions
        grid_rows = self.grid_size
        grid_cols = self.grid_size

        # Calculate the pixel spacing for the grid
        grid_step_x = int((img.shape[1] - 100) / grid_cols)
        grid_step_y = int((img.shape[0] - 100) / grid_rows)

        # Calculate the center point of the grid
        center_x = int(img.shape[1] / 2)
        center_y = int(img.shape[0] / 2)

        # Create an empty list to store the pixel tuples
        pixel_coordinates = []

        # Populate the list with equidistant pixel tuples
        for i in range(grid_rows):
            for j in range(grid_cols):
                # Calculate the coordinates of the current pixel
                x = center_x + (j - grid_cols // 2) * grid_step_x
                y = center_y + (i - grid_rows // 2) * grid_step_y

                # Set the current pixel to red
                pixel_coordinates.append((x, y))

                # Draw a circle at the current pixel
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        # Display the image
        # cv2.imshow("Grid of Pixels", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return pixel_coordinates
