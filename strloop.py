# Example - echo
# Take in a string. Return that string repeated ("echoed") a number of times equal to the length of the string.
# For example, "hello" would return "hellohellohellohellohello" since there are five letters in "hello".
def echo(s):
    new_str = ""
    for i in range(len(s)):
        new_str += s
    return new_str

# 1
# Take in a string. Return that string repeated ("echoed") a number of times equal to the length of the string.
# Each time the string echoes, remove one letter from the start of the string.
# Append the string "\n" after each repetition of the input. (\n creates a new line when you print it.)
# For example, echo_short("seeya") would return:
# seeya
# seey
# see
# se
# s
def echo_short(s):
    len_s = len(s)
    new_str = ""
    for i in range (len_s):
        new_str += s + "\n"
        s = s[:-1]
    return new_str

# 2
# Take in a string and determine if it contains only pairs of letters - first in lowercase, then uppercase.
# For example: pairs("aAbBcCdD") returns True. pairs("aABB") returns False. pairs("zZfF") returns True.
# An empty string should return True
# Hint: a while loop is really good at incrementing by more than one index at a time.
def pairs(s):
    # new_str = ""
    i = 0
    if len(s) % 2 == 1:
        return False
    elif s == "":
        return True
    while i < len(s):
        if not (s[i].lower() == s[i + 1].lower() and s[i].lower() == s[i] and s[i + 1].upper() == s[i + 1]):
            return False
        elif s[i].lower() == s[i + 1].lower() \
            and s[i].lower() != s[i] \
            and s[i + 1].upper() == s[i + 1]:
            return False
        i += 2
    return True
     
           

assert(pairs("aAbBcCdD") == True)
assert(pairs("aABB") == False)
assert(pairs("zZfF") == True)
assert(pairs("tTdDhHeE") == True)
assert(pairs("vVe") == False)
assert(pairs("") == True)
# 3
# Take in a string s and a number n, and return (s rotated by 1, n times), with "\n" after each rotation.
# To rotate a string, remove the first character and append it to the end of the string. Example: "abc" -> "bca" -> "cab"
# For example, spin("hey", 5) would return:
# eyh
# yhe
# hey
# eyh
# yhe
def spin(s, n):
    i = 0
    new_str = ""
    if s == "":
        return "\n" * n
    while i < n:
        s = s[1:] + s[0]
        new_str += s + "\n"
        i += 1
    return new_str  
    
assert(spin("hey", 5) == "eyh\nyhe\nhey\neyh\nyhe\n")
assert(spin("hey", 1) == "eyh\n")
assert(spin("hello", 0) == "")
assert(spin("world", 2) == "orldw\nrldwo\n")
assert(spin("a b", 2) == " ba\nba \n")
assert(spin("", 5) == "\n\n\n\n\n")
assert(spin("", 10) == "\n\n\n\n\n\n\n\n\n\n")
#remove 1st letter
#add it to the end of the string
#n = how many times it goes through the loop


# 4
# Take in two strings, which may be of inequal length.
# Return the two strings interwoven - one letter from each until both are together.
# For example, interweave("HELLO", "worlddd") would return "HwEoLrLlOddd"
# As a hint, remember that you need a new variable for each thing you want to keep track of.
def interweave(a, b):
    i = 0
    new_str = ""
    while i < len(a) and i < len(b):
        new_str += a[i] + b[i]
        i += 1
    new_str = new_str + a[i:] + b[i:]
    return new_str   

#take in 2 strings
# take first letter from a + first letter of b
# loop

# 5
# Take in a string, s. Return s, where letters inside stars ("*") are uppercased. If there are not an even number of stars, return None instead.
# For example, uppercase_stars("he*llo*") returns "heLLO". uppercase_stars("*i* am *here*") returns "I am HERE".
# For example, uppercase_stars("*i* am *here") returns None.
# Hint: to flip a boolean, use: my_bool = not my_bool
def uppercase_stars(s):
    a = s.count("*")
    if a % 2 == 1:
        return None
    elif a % 2 == 0:
        i = 0
        new_str = ""
        in_between = False
        while i < len(s):
            if s[i] == "*" :
                if in_between == True:
                   in_between = False
                else:
                    in_between = True
            elif in_between == True:
                new_str += s[i].upper()
            else:
                new_str += s[i]
            i += 1 
        return new_str
#1. if pass asterick u r in between
#2nd time i pass the asterick i am no longer in between
#loop
            
            
            
            
            
            
            
            
            
            
            
        
#if characters between * * make it upper
#return new string

