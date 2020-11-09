def find_duplicates(in_list):

    if not in_list:
        return 0, None

    repetitions = {}        # dictionary of values and how many times they repeat
    repetitions[None] = 0   # for if there is no maximum to avoid an error
    maximum = in_list[0]    # value with the most repetitions

    # count the duplications for every value in the input list
    for value in in_list:
       repetitions[value] = 0
       for val in in_list:
           if val == value:
               repetitions[value] += 1

       # if the current value has the most duplications, it is the current maximum
       if repetitions[value] > repetitions[maximum]:
           maximum = value
       if repetitions[value] == repetitions[maximum] and value != maximum:
           maximum = None
           repetitions[None] = repetitions[value]

    return repetitions[maximum], maximum