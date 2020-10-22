# 1 - Demo - Map/Reduce
# Return one string - each input string capitalized, concatentated together.
# concat_capitalized(["hello", "world", "hey"]) -> "HelloWorldHey"
# Note: The "map" is the capitalization, the "reduce" is the concatentation.
def concat_capitalized(strs):
    new_str = ""
    for s in strs:
        new_str += s.capitalize()
    return new_str

# 2 - Map
# Return a list containing each of the numbers in the input, squared.
# square_each([1, 2, 3]) -> [1, 4, 9]
# square_each([5, 10]) -> [25, 100]


def square_each(nums):
    first_list = []
    for i in range(len(nums)):
        square = nums[i] ** 2
        first_list.append(square)
    return first_list
# print(square_each([1,2,3]))


# 3 - Map/Filter
# Return a list of the strings that were all lowercase, converted to all uppercase.
# uppercase_lowers(["abc", "Def", "gHi", "jkl"]) -> ["ABC", "JKL"]
# uppercase_lowers(["Abcde", "defGH", "ijklm"]) -> ["IJKLM"]
# Reminder: to append a string to a list, use .append(), not +=
def uppercase_lowers(strs):
    user_list = []
    for i in range(len(strs)):
        if strs[i].islower() == True:
            user_list.append(strs[i].upper())
    return user_list 
#print(uppercase_lowers(["abc", "Def", "gHi", "jkl"])
            
        
 
# 4 - Map/Filter
# For each number in the input list, double it. If it's divisible by 10, include that doubled value in the output.
# tens_doubles([3, 5, 25, 8]) -> [10, 50]
# This is because 5 * 2 == 10 and 25 * 2 == 50, which are both divisible by 10
# tens_doubles([100, 50, 24, 10]) -> [200, 100, 20]
def tens_doubles(nums):
    user_list = []
    for i in range(len(nums)):
        if nums[i] % 5 == 0 :
            user_list.append(nums[i] * 2)
    return user_list
    # else:
    #     if len(nums) % 10 != 0:
    #         user_list.remove(new_list)
   
# 5 - Reduce
# Return the product (result of multiplication) of all numbers in the input list.
# product([1, 2, 3]) -> 6
# product([4, 5, 6, 0]) -> 0
def product(nums):
  result = 1
  for i in nums:
    result = result * i
  return result
   
# 6 - Map/Reduce
# Find the average "value" of the characters in the input string. You can find the value of one character by calling ord() on it.
# Return the average truncated to an integer.
# average_char("abc") -> 98
# This is because a = 97, b = 98, c = 99
# average_char("hello") -> 106
def average_char(s):
    user_list = []
    total = 0
    for i in range(len(s)):
        total += ord(s[i])
    s = int(total / len(s))
    return s
    
        

# 7 - Map/Reduce
# Return the sums of the squares of each number in the input list.
# sum_squares([2, 3, 4]) -> 29
# This is because 2**2=4, 3**2=9, 4**2=16. 4 + 9 + 16 = 29
# sum_squares([10, 10]) -> 200
def sum_squares(nums):
    user_list = []
    total = 0
    for i in range(len(nums)):
        square = nums[i] ** 2
        total += square
    return total
        

# 8 - Filter
# Returns only the cats from the input list.
# Input will be in the form "Cat: CatName" or "Dog: DogName". The names may have spaces.
# only_cats(["Cat: Jupiter", "Dog: Io", "Cat: Rodeo"]) -> ["Cat: Jupiter", "Cat: Rodeo"]
# only_cats(["Cat: Perry", "Dog: Tailings", "Dog: Big Guy"]) -> ["Cat: Perry"]
def only_cats(pets):
    user_list = []
    for i in range(len(pets)):
        letter = pets[i][0] #i is getting a specific element in array and 0 is getting specific char in string
        if letter == "C":
            user_list.append(pets[i])
    return user_list
            

        
    

# 9 - Filter/Reduce
# Return the sum of all values in the input list (first parameter) below the cutoff number (second parameter).
# total_below([5, 10, 30, 40], 30) -> 15
# This is because only 5 and 10 are below 30, so 5 + 10 = 15
# total_below([10, 40, 10, 50, 10, 60], 20) -> 30 
def total_below(vals, cutoff):
    user_list = []
    total = 0
    for i in range(len(vals)):
        if vals[i] < cutoff:
            total += vals[i]
    return total    
    
    
    
# 10 - Filter/Reduce
# Return the sum of only the even numbers in the input
# sum_evens([2, 3, 4, 5, 6]) -> 12
# sum_evens([10, 11, 20, 21]) -> 30
def sum_evens(nums):
    user_list = []
    total = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total
            
            
            
            
