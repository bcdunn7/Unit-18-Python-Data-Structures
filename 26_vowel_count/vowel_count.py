def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lower_phrase = phrase.lower()

    counter = {}

    vowels = 'aeiou'

    #this works just with predetermined order of vowels
    # for char in vowels:
    #     num = lower_phrase.count(char)
    #     if num != 0:
    #         counter[f"{char}"] = num
    
    

    for char in lower_phrase:
        keys = counter.keys()
        t_keys = tuple(keys)
        if vowels.count(char) != 0 and t_keys.count(char) == 0:
            num = lower_phrase.count(char)
            counter[f"{char}"] = num

    return counter
