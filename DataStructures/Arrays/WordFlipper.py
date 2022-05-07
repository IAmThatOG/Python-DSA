def word_flipper(our_string: str):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    # TODO: Write your solution here
    strArray = our_string.split(" ")
    newString = ""
    for i in range(len(strArray)):
        iString = strArray[i]
        for j in range(len(iString)):
            newString += iString[(len(iString) - 1) - j]
            if j + 1 == len(iString):
                newString += " "
    return newString.strip()


def word_flipper(our_string: str):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    # TODO: Write your solution here
    strArray = our_string.split(" ")
    newString = ""
    for i in range(len(strArray)):
        iString = strArray[i]
        for j in range(len(iString)):
            newString += iString[(len(iString) - 1) - j]
            if j + 1 == len(iString):
                newString += " "
    return newString.strip()
    
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")