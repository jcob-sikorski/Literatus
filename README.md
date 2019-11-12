# Literatus
Literatus is primitive tool for recognizing only uppercase letters. It starts by binarizing image from RGB values to 0s and 1s for white and black in matrix. Then it finds finds letters as seperate objects, by coonectivity between up and left neighbours, assigning them unique values, for example ABC - > 123 in matrix.


Literatus
|
|
|main.py
        |
        |
        |con_algo.py
                    |bw_pixels_to_matrix.py
                                          |
                                          |
                                          |rotate90Clockwise.py
                    |dig_val.py
                    |rotate90Clockwise.py
        |
        |
        |black_white.py

Instruction:
1. Install pillow
2. Install python 3.7.4
3. Install matplotlib, numpy, matlab

How to use?

1. Download greyscale image
2. Add image to project directory
3. Open main.py
4. Specify path to image
5. Evaluate how many letters are in the image. - Type it to terminal.
6. Click enter.

Unfortunately the tool only recognises seperate letters, objects too.
