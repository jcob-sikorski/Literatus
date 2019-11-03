def bw_pixels_to_matrix():
    'Returns matrix with 0s for white and 1s for black pixels.'
    
    from PIL import Image

    from rotate_matrix import rotate90Clockwise
    
    im = Image.open(r'C:\Users\jmsie\Dev\Projects\normalized.png')

    # coordinates (x, y)
    counter = 0

    matrix = []
    row = []

    black = 1

    print(im.size[0])
    print(im.size[1])
    # loops through pixels in image and creates matrix of black(1) and white(0) values for pixel
    for xi in range(im.size[0]):
        for yi in range(im.size[1]):
            
            counter += 1

            if counter == im.size[0]:
                
                counter = 0
                
                matrix.append(row)
                row = []
            
            pixel = im.getpixel((yi, xi))
            
            if pixel[:3] == (255, 255, 255):
                row.append(0)

            elif pixel[:3] == (0, 0, 0):
                row.append(1)

    matrix[0].append(0)

    return matrix
