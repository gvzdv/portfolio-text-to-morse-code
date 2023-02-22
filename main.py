# python3

import json

# Receive the string as input and make it lower case as the keys in the dictionary are in the lower case
text_string = input("Please enter your text: ").lower()

# Convert the string to Morse code using three spaces between letters and seven spaces between words
# as per timing conventions. Collect the symbols that do not have Morse code designations and inform the user.
with open("morse_encode.json", "r") as file:
    encode = json.load(file)
    morse_string = ""
    missing_symbols = ""
    for char in text_string:
        if char in encode:
            morse_string += f"{encode[char]}   "
        elif char == " ":
            morse_string += "       "
        else:
            missing_symbols += f"{char} "
    print(f"Your Morse code is {morse_string}")
    print(f"The following symbols could not be included into your Morse code: {missing_symbols}")

