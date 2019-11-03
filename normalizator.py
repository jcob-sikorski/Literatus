def black_white_im():
    '''
    Function changes image to new image with only black and white colours. 0s and 1s
    '''

    # library with necessary functions to work with image
    from PIL import Image

    # to delete processed image
    # from os import remove

    # contains set image
    path = str(input(r'Please specify the path to image: '))

    im = Image.open(path)

    # contains set image with alpha value
    rgb_im = im.convert('RGB')
    re_rgb_im = rgb_im.resize((100, 100), 0)

    # lower bound for whiteness
    white_threshold = 50

    print('Normalizing image...')

    # transforms to black-white
    # width
    for x in range(re_rgb_im.size[0]):

        # height
        for y in range(re_rgb_im.size[1]):

            # tuple containing rgb values
            pixel = re_rgb_im.getpixel((x, y))
        
            # if rgb value is less than 50 then change it to white
            if pixel[:3] > (white_threshold, white_threshold, white_threshold):
                re_rgb_im.putpixel((x, y), (255, 255, 255))

            # else change it to black
            else:
                re_rgb_im.putpixel((x, y), (0, 0, 0))
    
    re_rgb_im.save('normalized.png')

    print('Image processed and normalized!')
