'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    list_of_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if (letter in list_of_alphabet) == True:
        for i in list_of_alphabet:
            if list_of_alphabet.index(i) == (shift % 26):
                return list_of_alphabet[(list_of_alphabet.index(letter) + shift) % 26]
            else:
                continue
    else:
        return " "
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def caesar_cipher(message, shift):
    list_of_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i,letter in enumerate(message):
        if (letter in list_of_alphabet) == True:
            print(list_of_alphabet[(list_of_alphabet.index(letter) + shift) % 26],end="")
            continue
        else:
            print(" ",end="")
    return ""
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def shift_by_letter(letter, letter_shift):
    list_of_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if (letter in list_of_alphabet) == True:
        for i in list_of_alphabet:
            if list_of_alphabet.index(i) == (list_of_alphabet.index(letter_shift) % 26):
                return list_of_alphabet[(list_of_alphabet.index(letter) + list_of_alphabet.index(letter_shift)) % 26]
            else:
                continue
    else:
        return " "
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def vigenere_cipher(message, key):
    list_of_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter_of_message_separated = ""
    letter_of_key_separated = ""
    x = 0
    for i,letter in enumerate(message):
        if (letter in list_of_alphabet) == True:
            letter_of_message_separated += (list_of_alphabet[(list_of_alphabet.index(letter)) % 26])
        else:
            letter_of_message_separated += " "
    for i,letters in enumerate(key):
        if (letters in list_of_alphabet) == True:
            letter_of_key_separated += str((list_of_alphabet.index(letters))) + " "
            array_of_key = letter_of_key_separated.split()
        else:
            letter_of_key_separated += " "
    while x < len(message):
        if (letter_of_message_separated[x] in list_of_alphabet):
            print(((list_of_alphabet[(list_of_alphabet.index(letter_of_message_separated[x]) + int((array_of_key[x % len(key)]))) % 26])), end="")
        else:
            print(" ", end="")
        x+=1
    return ""
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def scytale_cipher(message, shift):
    i=0
    cryptic_message_indexed=""
    msg_added_underscores=""
    if len(message) % shift == 0:
        for i,characters in enumerate(message):
            cryptic_message_indexed+=message[(i // shift) + (len(message) // shift) * (i % shift)]
            i+=1
    else:
        msg_added_underscores = (message+"_"*((shift -(len(message)% shift))))
        for i,characters in enumerate(msg_added_underscores):
            cryptic_message_indexed+=msg_added_underscores[(i // shift) + (len(msg_added_underscores) // shift) * (i % shift)]
            i+=1
    return cryptic_message_indexed
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def scytale_decipher(message, shift):
    i=0
    deciphered_message_indexed=""
    if len(message) % shift == 0:
        for i,characters in enumerate(message):
            deciphered_message_indexed+=message[(((i * shift) + (len(message) * shift) * (i // shift)) % len(message))+(i // (len(message) // shift))]
            i+=1
    return deciphered_message_indexed
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass
