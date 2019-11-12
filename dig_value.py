def dig_val(key, dictionary):
  '''
  Finds smallest object identity for every pixel in letter.
  '''
    if key == dictionary[key]:
        return dictionary[key]

    else:
        return dig_val(dictionary[key], dictionary)
