def sort(in_string):
    # convert to list for ease of swapping characters
    in_string = list(in_string)

    # flag variable
    alphabetized = False
    while not alphabetized:
        alphabetized = True # will remain True if no values are swapped

        for i in range(len(in_string)):
            if i == 0:
                continue

            # check if every character is lower on the alphabet than the previous
            if ord(in_string[i]) < ord(in_string[i - 1]):
                # swap the 2 characters
                placeholder = in_string[i]
                in_string[i] = in_string[i - 1]
                in_string[i - 1] = placeholder
            
                alphabetized = False

    # convert back to string
    in_string = ''.join(in_string)

    # return result
    return in_string
