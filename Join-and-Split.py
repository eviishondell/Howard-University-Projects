# 1 - Demo
# This is the same as str's title() method, but it's a good example
# Take in a string and capitalize each word. Assume the string will not have punctuation.
def capitalize_each_word(s):
    new_list = []
    s_list = s.split(' ')
    for word in s_list:
        new_list.append(word.capitalize())
    return ' '.join(new_list)


# 2
# Take in a comma-separated string of floats.
# Return a new comma-separated string only containing the items less than the cutoff.
# keep_below('10,20.5,4,3,6,300', 10) returns '4,3,6'
# keep_below('1,2,3,4,5,6', 4) returns '1,2,3'
def keep_below(s, cutoff):
    new_list = []
    c = s.split(",")
    if s == "":
        return s
    for i in range(len(c)):
        if float(c[i]) < cutoff:
            new_list.append(c[i])
    return ",".join(new_list)

            
            


# 3
# Take in a underscore-separated string of floats.
# Return the sum of all of the items above the cutoff.
# sum_above('1_2_3_4_5', 3) returns 9
# sum_above('5_10.5_3_20') returns 30.5
def sum_above(s, cutoff):
    new_list = []
    c = s.split("_")
    if s == "":
        return 0
    for i in range(len(c)):
        if float(c[i]) > cutoff:
            new_list.append(float(c[i]))
    d = sum(new_list)
    return d
        


# 4
# Take in a string s, and a string word. Remove all instances of the word from s, and return that value as a string.
# Assume there will be no punctuation in the input.
# remove_word('I got a new carpet for my car', 'car') returns 'I got a new carpet for my'
# remove_word('a b c abc', 'b') returns 'a c abc'
def remove_word(s, word):
    #s = hi im evolone
    #word = im
    #new = hi evolone
    new_list = []
    split_list = s.split(" ")
    for i in range(len(split_list)):
        # [hi , im , evolone]
        if split_list[i] != word:
            new_list.append(split_list[i])
            #split_list.remove(split_list[i])
    s = " ".join(new_list)
    return s

# 5
# Take in a string s, and sort it in reverse-alphabetical order. Return a string.
# sort_words('a b c') returns 'c b a'
# sort_words('hello world hey there') returns 'world there hey hello'
def sort_words_rev(s):
    # new_list = []
    split_list = s.split(" ")
    split_list.sort(reverse=True)
        # new_list.append(reverse)
    s = " ".join(split_list)
    return s
#create my new list
#convert STRING S to list
#create a new list with it in reverse alphabetical order
#join it and make it a STRING
#return it


# 6
# Take in a series of game scores and return the total score of the highest scoring game.
# Each game is represented by two int values with a dash between them.
# e.g. 5-6 means one team scored 5 points and the other team scored 6 points. The total for this game is 11 points.
# e.g. 1-8 means one team scored 1 point and the other team scored 8 points. The total for this game is 9 points.
# Each game is separated by a "%" sign. So "1-4%6-7" has two games, one with 5 total points (1 + 4) and the other with 13 (6 + 7)
# max_game_score('1+4 6+7') [5, 13] returns 13
# max_game_score('1-2%4-3%2-2') returns 7
def max_game_score(s):
    if s == "":
        return 0
    sum_list = []
    split_list = s.split("%")
    for i in range(len(split_list)):
        plus = split_list[i].split("-")
        sum_list.append(int(plus[0]) + int(plus[1]))
    sum_list.sort(reverse = True)
    return sum_list[0]
    
    
    
    #eval function takes in string and solves while sum will only work with a list of numbers
    
    
#s = string of scores
# replace the - with +  ('1+2%4+3%2+2')
#split list by %      ['1+2','4+3','2+2']    [1,2]
#put the numbers in a list
#sort them in place from greatest to least
#return list[0]
#return game with the highest sum


#split by plus sign then convert strings to int
    
    
