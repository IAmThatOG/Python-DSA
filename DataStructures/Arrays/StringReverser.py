def string_reverser_one(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    index = len(our_string) - 1
    newString = ""
    for i in range(index, -1, -1):
        newString += our_string[i]
    return newString

print ("Pass" if ('retaw' == string_reverser_one('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser_one('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser_one('The house code is: 2343')) else "Fail")


def string_reverser_two(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    newString = ""
    for i in range(len(our_string)):
        # f = f'i ==> {i}'
        # print(f)
        newString += our_string[(len(our_string)-1) - i];
    return newString

print ("Pass" if ('retaw' == string_reverser_two('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser_two('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser_two('The house code is: 2343')) else "Fail")