def all_except_first(s):
    """Return the string without the first character.
    all_except_first("hello") returns "ello" """
    return s[1:]
    #pass

def last_n_chars(s, n):
    """Return the final n chars of s.
    last_n_chars("hello world", 3) returns "rld"
    You can assume that s is always at least n characters long. """
    return s[-n:]
    #pass
#int division is // and regular division is /  
def second_half(s):
    """Returns the second half of the string (including the middle, if the string is an odd length.)
    second_half("catsanddogs") returns "nddogs" """
    if len(s) % 2 == 0:
        length = len(s) / 2
        new_length =int(length)
        return s[new_length:]
    else:
        if len(s) % 2 != 0: #means its odd bc there is a remainder
            length = len(s) / 2
            newer_length = int(length)
            return s[newer_length:]
    #pass

def after_symbol(s, sym):
    """Return all of the characters after the character given
    after_symbol("eseidohl@google.com", "@") returns "google.com"
    after_symbol("eseidohl@google.com", ".") returns "com"
    You can assume that sym is always one character and always exists in s.
    Hint: What does .find() do?"""
    text = s.find(sym)
    return s[text + 1:]
  
    #find the command
    #then we use the [command:]
    
    
    #pass
#geoffrey helped we with this
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
def middle_n(s, n):
    """Returns the middle n characters from a string.
    middle_n("abcdcba", 3) returns "cdc"
    Default toward the end of the list if the selection does not line up exactly.
    middle_n("abcdcba", 4) returns "cdcb"
    This one is more difficult! Use intermediate variables to keep track of values."""
    if s.find(" ") != -1:
        new_n = n + 1
        left = len(s) / new_n
        lleft = int(left)
        right = s[lleft + 2:]
        new = right[:n]
        return new
    elif (len(s) - n) != even:
        new_n = n + 1
        left = len(s) / new_n
        lleft = int(left)
        right = s[lleft + 1:]
        new = right[:n]
        return new
    else:
        new_n = n + 1
        left = len(s) / new_n
        lleft = int(left)
        right = s[lleft + 1:]
        new = right[:n + 1]
        return new
        
     
        


