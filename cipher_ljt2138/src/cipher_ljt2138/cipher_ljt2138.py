def cipher(text, shift, encrypt=True):
    """
    Shifts alphabetic characters in a string by a given amount such
    as with a Caesar cipher.

    Parameters
    ----------
    text : str
      A string to be shifted. Non-alphabetic letters are unchanged.
    shift : int
      The number of positions to shift letters in the text.
    encrypt : bool
      Whether to shift in the positive direction rather than the 
      negative direction (default True).

    Returns
    -------
    str
      The shifted text.

    Examples
    --------
    >>> cipher("Hi all!", 2)
    'Jk cnn!'
    
    
    >>> cipher("Jk cnn!", 2, encrypt=False)
    'Hi all!'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text