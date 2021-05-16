def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    keys = list(d.keys())

    min_k = keys[0]
    max_k = keys[0]

    for key in keys:
        if key < min_k:
            min_k = key
        if key > max_k:
            max_k = key
    
    return (min_k, max_k)