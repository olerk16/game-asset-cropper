# import cv2
# import numpy as np
# from PIL import Image

# def remove_white_background(image_path, output_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image was loaded successfully
#     if image is None:
#         print(f"Error: Unable to load image at {image_path}. Please check the file path and try again.")
#         return
    
#     # Convert to RGBA
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

#     # Create a mask where white pixels (background) are detected
#     # Define the lower and upper range for white color
#     lower_white = np.array([240, 240, 240, 255])
#     upper_white = np.array([255, 255, 255, 255])
    
#     # Create the mask with the specified range
#     mask = cv2.inRange(image, lower_white, upper_white)

#     # Invert the mask to segment the subject
#     mask = cv2.bitwise_not(mask)

#     # Make the background transparent using the mask
#     image[mask == 0] = (0, 0, 0, 0)

#     # Save the image with transparency
#     output_image = Image.fromarray(image)
#     output_image.save(output_path, "PNG")
#     print(f"Image saved with transparent background at {output_path}.")

# if __name__ == "__main__":
#     # Use the correct file name for your input image
#     input_image_path = '/Users/coltenkrelo/Desktop/python-asset-crop/image_input.jpg'  # Correct file path
#     output_image_path = 'output_image.png'
#     remove_white_background(input_image_path, output_image_path)


import cv2
import numpy as np
from PIL import Image
import os

def remove_white_background(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}. Please check the file path and try again.")
        return
    
    # Convert to RGBA
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    # Create a mask where white pixels (background) are detected
    lower_white = np.array([240, 240, 240, 255])
    upper_white = np.array([255, 255, 255, 255])
    
    # Create the mask with the specified range
    mask = cv2.inRange(image, lower_white, upper_white)

    # Invert the mask to segment the subject
    mask = cv2.bitwise_not(mask)

    # Make the background transparent using the mask
    image[mask == 0] = (0, 0, 0, 0)

    # Save the image with transparency
    output_image = Image.fromarray(image)
    output_image.save(output_path, "PNG")
    print(f"Image saved with transparent background at {output_path}.")

if __name__ == "__main__":
    # Define the input directory containing the images
    input_directory = '/Users/coltenkrelo/Desktop/python-asset-crop/'
    output_directory = '/Users/coltenkrelo/Desktop/python-asset-crop/output/'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # You can add more image formats here
            input_image_path = os.path.join(input_directory, filename)
            output_image_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}_output.png')

            # Process each image to remove the white background
            remove_white_background(input_image_path, output_image_path)