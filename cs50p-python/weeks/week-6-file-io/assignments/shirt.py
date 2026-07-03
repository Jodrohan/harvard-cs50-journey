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