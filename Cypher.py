def cypher(text): #Function for a cypher that will replace each letter or number with the 15th value along
    new_string = ""
    for character in text:
        ascii_value = ord(character) 
        #ord() converts the character into its ascii value
        if ascii_value >= 108 and ascii_value <= 126: 
            # Dealing with lowercase characters that will loop
            new_character_value = (ascii_value + 116) - 127
            new_string += chr(new_character_value) 
            #chr converts a number into an ascii character


        elif ascii_value >= 97 and ascii_value <= 107: 
            # Dealing with lowercase characters that will not loop
            new_character_value = ascii_value + 15
            new_string += chr(new_character_value)

        elif ascii_value >= 76 and ascii_value <= 90: 
            # Dealing with uppercase characters that will loop
            new_character_value = (ascii_value + 116) - 127
            new_string += chr(new_character_value)

        elif ascii_value >= 65 and ascii_value <= 75: 
            # Dealing with uppercase characters that will not loop
            new_character_value = ascii_value + 15
            new_string += chr(new_character_value)

        elif ascii_value >= 48 and ascii_value <= 52: 
            # Dealing with the loop for numbers between 0 and 4 
            new_character_value = (ascii_value + 15) - 10
            new_string += chr(new_character_value)

        elif ascii_value >= 53 and ascii_value <= 57: 
            # Dealing with the loop for numbers between 5 and 9 
            new_character_value = (ascii_value + 10) - 15
            new_string += chr(new_character_value)

        else:
            new_character_value = ascii_value 
            # All characters that do not meet any of the criteria above remain the same
            new_string += chr(new_character_value)

    return new_string

test = input("Enter a sentence to encrypt: ")

print(cypher(test))

    
