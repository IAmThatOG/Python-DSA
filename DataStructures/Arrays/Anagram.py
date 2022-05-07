def anagram_checker(str1: str, str2: str):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    str1 = str1.strip().replace(" ", "").lower();
    str2 = str2.strip().replace(" ", "").lower();

    str1Sorted = sorted(str1)
    str2Sorted = sorted(str2)
    if(len(str1Sorted) != len(str2Sorted)):
        return False
    if(str1Sorted != str2Sorted):
        return False
    return True

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")