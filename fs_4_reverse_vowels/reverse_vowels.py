def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiouAEIOU'
   
    s_lst = list(s)

    i = 0
    j = len(s) - 1

    while i < j:
        if s_lst[i] not in vowels:
            i += 1
        elif s_lst[j] not in vowels:
            j -= 1
        else:
            s_lst[i], s_lst[j] = s_lst[j], s_lst[i]
            i += 1
            j -= 1

    return "".join(s_lst)