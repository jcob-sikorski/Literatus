def con_algo():
    'Distinguishes n letters from black and white pixels (1s, 0s) in given image and forms them as letters with their real number counting left to right.'

    number_from_user = int(input('How many letters are in the image? number = '))

    import numpy as np

    from matplotlib import pyplot as plt

    from random import randint

    from PIL import Image # for work with image

    from bw_pixels_to_matrix import bw_pixels_to_matrix as bw # returns matrix

    from dig_val import dig_val # digs into the deepest value in connected keys in dictionary

    from heapq import nlargest # finds n largets objects in matrix

    from rotate_matrix import rotate90Clockwise

    im = Image.open('normalized.png')

    matrix = bw()#[[randint(0,1) for i in range(7)] for y in range(7)]


    #plt.imshow(matrix, interpolation='nearest')
    #plt.colorbar()
    #plt.show()

    # x is for counting independent elements in image
    x = 0

    width, height = im.size

    # dictionary with key (number from main algorithm) and value (number which is the lowest number, which then is converted into real number)
    equivalency = {}

    # checking connectivity of black pixels
    # (index, row)
    for ri, row in enumerate(matrix):
        # (index, element)
        for ei, elem in enumerate(row):
            # if element is black checks if it has some neighbours
            if matrix[ri][ei] > 0:
                # if it's not first row or column check top and left neighbours
                if ri > 0 and ei > 0:
                    # if left and top neighbour are equal to 0, add new object
                    if matrix[ri][ei-1] == 0 and matrix[ri-1][ei] == 0:
                        x += 1
                        matrix[ri][ei] = x
                        equivalency[matrix[ri][ei]] = matrix[ri][ei]
                    # elif left and top neighbour aren't equal to 0, make the element the same as element with smaller value
                    elif matrix[ri][ei-1] > 0 and matrix[ri-1][ei] > 0:
                        matrix[ri][ei] = min(matrix[ri][ei-1], matrix[ri-1][ei])

                        if matrix[ri][ei-1] == matrix[ri-1][ei]:
                            pass
                        else:
                            equivalency[max(matrix[ri][ei-1], matrix[ri-1][ei])] = matrix[ri][ei]
                        
                    # elif left or top neighbour is bigger than 0, make the element the same as element which isn't 0
                    elif matrix[ri][ei-1] > 0 or matrix[ri-1][ei] > 0:
                        matrix[ri][ei] = equivalency[max(matrix[ri][ei-1], matrix[ri-1][ei])]
                # if it's first column check only top neighbour
                elif ei == 0 and ri > 0:
                    # if top neighbour > 0 make element the same as him
                    if matrix[ri-1][ei] > 0:
                        matrix[ri][ei] = matrix[ri-1][ei]
                    # else, add new object
                    else:
                        x += 1
                        matrix[ri][ei] = x
                        equivalency[matrix[ri][ei]] = matrix[ri][ei]
                # while it's first row, checks only left neighbour
                elif ri == 0 and ei > 0:
                    # if left neighbour > 0 make element the same as him
                    if matrix[ri][ei-1] > 0:
                        x += 1
                        matrix[ri][ei] = matrix[ri][ei-1]
                        equivalency[matrix[ri][ei]] = matrix[ri][ei]
                    # else, add new object
                    else:
                        x += 1
                        matrix[ri][ei] = x
                        equivalency[matrix[ri][ei]] = matrix[ri][ei]
                # finally if element is first in matrix, pass 
                else:
                    pass

    #plt.imshow(matrix, interpolation='nearest')
    #plt.colorbar()
    #plt.show()

    # finds the lowest number in equivalency dictionary
    for ri, row in enumerate(matrix):
        for ei, elem in enumerate(row):
            if matrix[ri][ei] > 0:    
                matrix[ri][ei] = dig_val(matrix[ri][ei], equivalency)


    row = [i for i in matrix]
    elements = []

    for r in row:
        for e in r:
            elements.append(e)

    unik = []

    unique = []

    for elem in elements:
        if elem not in unik:
            unik.append(elem)

    for i in unik:
        if i == 0:
            pass
        else:
            unique.append(i)

    # dictionary with true numbers of objects
    true_object = {}
    
    for i in unique:
        true_object[i] = unique.index(i) + 1

    for ri, row in enumerate(matrix):
        for ei, elem in enumerate(row):
            if matrix[ri][ei] > 0:
                matrix[ri][ei] = true_object[matrix[ri][ei]]#dig_val(matrix[ri][ei], true_object)

    #print('\n')
    print(true_object)

    #print('\n')

    # final approval

    print('\n')

    #for i in matrix:
    #    print(i)

    # dictionary which stores number of every pixel connected with specific object
    count_objects = {}

    # adding results of counting to dict(count_objects)
    for key in true_object:
        count_objects[true_object[key]] = sum(row.count(true_object[key]) for row in matrix)

    print(count_objects)

    # dictionary with only true letters not for example fake letters like individual black pixels in image
    n_highest_letters = nlargest(number_from_user, count_objects, key = count_objects.get)

    n_highest_letters_sorted = sorted(n_highest_letters)  

    copy_of_n_highest_letters_sorted = list(n_highest_letters_sorted)

    print(n_highest_letters_sorted)

    # dict with coordinates for every edge of letter, letter: [(top), (left), (bottom), (right)]
    coordinates = {}

    for i in n_highest_letters_sorted:
        coordinates[i] = []

    for row_index, row in enumerate(matrix):
        if not n_highest_letters_sorted: break
        for column_index, value_present in enumerate(row):
            if not n_highest_letters_sorted: break
            for value_sought_index, value_sought in enumerate(n_highest_letters_sorted):
                if value_present == value_sought:
                
                    coordinates.setdefault(value_sought, []).append(row_index)#((row_index, column_index))
                    n_highest_letters_sorted.pop(value_sought_index)
                    break

    #print('top_coordinates ', coordinates)

    im_90 = rotate90Clockwise(matrix)

    n_highest_letters_sorted = sorted(n_highest_letters) 

    for row_index, row in enumerate(im_90):
        if not n_highest_letters_sorted: break
        for column_index, value_present in enumerate(row):
            if not n_highest_letters_sorted: break
            for value_sought_index, value_sought in enumerate(n_highest_letters_sorted):
                if value_present == value_sought:

                    coordinates.setdefault(value_sought, []).append(row_index)#((len(matrix[0]) - column_index, row_index))

                    n_highest_letters_sorted.pop(value_sought_index)
                    break

    #print('left_coordinates ', coordinates)
    #
    #plt.imshow(im_90, interpolation='nearest')
    #plt.title('im90')
    #plt.colorbar()
    #plt.show()

    im_180 = rotate90Clockwise(im_90)

    n_highest_letters_sorted = sorted(n_highest_letters)

    for row_index, row in enumerate(im_180):
        if not n_highest_letters_sorted: break
        for column_index, value_present in enumerate(row):
            if not n_highest_letters_sorted: break
            for value_sought_index, value_sought in enumerate(n_highest_letters_sorted):
                if value_present == value_sought:

                    coordinates.setdefault(value_sought, []).append(len(matrix[0]) - row_index)#((len(matrix[0]) - row_index, len(matrix[0]) - column_index))

                    n_highest_letters_sorted.pop(value_sought_index)
                    break

    #print('bottom_coordinates ', coordinates)
#
    #plt.imshow(im_180, interpolation='nearest')
    #plt.title('im180')
    #plt.colorbar()
    #plt.show()

    im_270 = rotate90Clockwise(im_180)

    n_highest_letters_sorted = sorted(n_highest_letters) 

    for row_index, row in enumerate(im_270):
        if not n_highest_letters_sorted: break
        for column_index, value_present in enumerate(row):
            if not n_highest_letters_sorted: break
            for value_sought_index, value_sought in enumerate(n_highest_letters_sorted):
                if value_present == value_sought:

                    coordinates.setdefault(value_sought, []).append(len(matrix[0]) - row_index)#((column_index, len(matrix[0]) - row_index))

                    n_highest_letters_sorted.pop(value_sought_index)
                    break


    print('coordinates ', coordinates)
#
    #plt.imshow(im_270, interpolation='nearest')
    #plt.title('im270')
    #plt.colorbar()
    #plt.show()

    plt.imshow(rotate90Clockwise(matrix), interpolation='nearest')
    plt.title('im')
    plt.colorbar()
    plt.show()

    bounding_box_for_each_letter = {}

    print(f'copy_of_n_highest_letters_sorted   {copy_of_n_highest_letters_sorted}')

    for i in copy_of_n_highest_letters_sorted:
        bounding_box_for_each_letter[i] = []

    print(f'bounding_box_for_each_letter   {bounding_box_for_each_letter}')

    counter = 0

    ro = []

    for i in copy_of_n_highest_letters_sorted:
        top = coordinates[i][0]
        left = coordinates[i][1]
        bottom = coordinates[i][2]
        right = coordinates[i][3]

        print(top, left, bottom, right)
        print(i)

        for ri, row in enumerate(matrix):
            for ei, elem in enumerate(row):
                if top <= ri and ri <= bottom and left <= ei and ei < right:
                    counter += 1

                    if counter == int(right- left):
                
                        counter = 0
                        bounding_box_for_each_letter.setdefault(i, []).append(list(ro))
                        ro = []

                    ro.append(elem)
    
    for i in bounding_box_for_each_letter[4]:
        print(i)

    #horizontal_cells = 10
	#vertical_cells = 10
	#horizontal_ratio = im.size[0]//horizontal_cells
	#vertical_ratio = im.size[1]//vertical_cells
	#values = []
	#for i in range(horizontal_cells):
	#	for j in range(vertical_cells):
	#		cellsum=0
	#		for x in range(horizontal_ratio):
	#			for y in range(vertical_ratio):
	#				cellsum+=im.getpixel(((i*horizontal_ratio)+x,(j*vertical_ratio)+y))[0]
	#		cellvalue = cellsum//(horizontal_ratio*vertical_ratio)
	#		values.append(cellvalue)

    return coordinates
    # crop(left, upper, right, and lower)

con_algo()
