def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    left_count = 0
    right_count = 0

    for par in parens:
        if right_count > left_count:
            return False
        else:
            if par == "(":
                left_count += 1
            elif par == ")":
                right_count += 1
    
    if left_count != right_count:
        return False

    return True
