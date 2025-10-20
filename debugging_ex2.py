# Run a non-working code to gain experience debugging.

# Run the debugger and make changes until the code is bug-free, according to the
# docstring.

def check_3string_sequence(seq):
    '''
    Check that all three items in the sequence are unique.

    Parameters
    ----------
    seq: iterable
        An iterable of 3 strings

    Returns
    -------
    is_unique: bool
        True for strings with 3 unique items, False otherwise
    '''
    # First, check sequence length
    assert len(seq) == 3
    # Next, check to make sure that all items in the sequence are strings
    for item in seq:
        assert isinstance(item, str)
    # Unpack arguments and check sequence
    (s, s1, s2) = seq
    is_unique = (s != s1 != s2)
    return is_unique


if __name__ == '__main__':
    str = 'cat'
    str1 = 'dog'
    str2 = 'cow'
    is_unique = check_3string_sequence((str, str1, str2))
    print('Sequence 1 unique?', is_unique)

    str3 = 'bat'
    str4 = ''
    str5 = 'bat'
    is_unique = check_3string_sequence((str3, str4, str5))
    print('Sequence 2 unique?', is_unique)