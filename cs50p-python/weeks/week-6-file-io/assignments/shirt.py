"""
Assignment: CS50 P-Shirt
Objective: 
    Read an input image, resize and crop it to exactly match the dimensions 
    of 'shirt.png', overlay the shirt onto the image, and save the result.

Requirements:
    1. Command-line Arguments: The program must accept exactly two 
       command-line arguments via `sys.argv`:
       - The first is the path to the input photo (e.g., before.jpg).
       - The second is the path to the output photo (e.g., after.jpg).
    2. Validation & Error Handling:
       - Exit using `sys.exit` if the user provides too few or too many arguments.
       - Exit if the input file does not exist (FileNotFoundError).
       - Exit if the file extensions are not valid (.jpg, .jpeg, .png).
       - Exit if the input file extension does not exactly match the output 
         file extension (case-insensitive).
    3. Image Processing (PIL/Pillow):
       - Load 'shirt.png' using `Image.open`.
       - Load the input image.
       - Use `ImageOps.fit` to resize/crop the input image to match the 
         shirt's `.size` attribute.
       - Use `Image.paste` to overlay the shirt onto the resized input image.
    4. Output:
       - Save the generated image to the path specified in the second argument.

Usage:
    $ python shirt.py before.jpg after.jpg
"""
import sys
import os
from PIL import Image, ImageOps


def main():

    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")

    accepted_extensions = (".jpg", ".jpeg", ".png")

    if not sys.argv[1].lower().endswith(accepted_extensions):
        sys.exit("File not supported")

    if not sys.argv[2].lower().endswith(accepted_extensions):
        sys.exit("File not supported")

    file_extension1 = os.path.splitext(sys.argv[1])[1].lower()
    file_extension2 = os.path.splitext(sys.argv[2])[1].lower()

    if file_extension1 != file_extension2:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")

    output = ImageOps.fit(input_image, shirt.size)
    output.paste(shirt, shirt)
    output.save(sys.argv[2])


if __name__ == "__main__":
    main()