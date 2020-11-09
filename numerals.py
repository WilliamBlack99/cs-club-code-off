# I -> 1
# V -> 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000
def convert_numerals(numerals):
    value = 0

    # ensure that every character in the input is a roman numeral
    for n in numerals:
        if n != "I" and n != "V" and n != "X" and n != "L" and n != "C" and n != "D" and n != "M":
            return False

    # create a list of the integer value of each numeral
    numerals_values = []
    for character in numerals:
      if character == "I":
         numerals_values.append(1)
      elif character == "V":
          numerals_values.append(5)
      elif character == "X":
          numerals_values.append(10)
      elif character == "L":
          numerals_values.append(50)
      elif character == "C":
        numerals_values.append(100)
      elif character == "D":
          numerals_values.append(500)
      elif character == "M":
          numerals_values.append(1000)

    # add values in the list together to get the total value
    for i in range(len(numerals_values)):
        # if the previous number is smaller, undo its addition and subtract it
        if i != 0:
            if numerals_values[i - 1] < numerals_values[i]:
                value -= 2*numerals_values[i - 1]

        # add the current value
        value += numerals_values[i]

    # return the result
    return value
