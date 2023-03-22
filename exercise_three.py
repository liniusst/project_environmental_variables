# write a function that accepts an encoded string as a parameter. 
# This string will contain a first name, last name, and an id.Values in the string can be separated by any number of zeros. 
# The id is a numeric value but will contain no zeros. The function should parse the string and return a 
# Python dictionary that contains the first name, last name, and id values.An example input would be “Robert000Smith000123”. 
# The function should return the following using that input:{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

def get_value(encoded_string: str):
    word_list = []
    word = ""
    for char in encoded_string:
        if char != "0":
            word += char
        else:
            if len(word) > 0:
                word_list.append(word)
                word = ""
    if len(word) > 0:
        word_list.append(word)
    return word_list


print(get_value("00Robert00000Smith000123"))