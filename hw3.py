# PROBLEM 1

def power(input, power):
    input1 = 1
    for i in range(power):
        input1 = input1 * input
    print(input1)
    return [input1]

"""
input1 or input' = 1 since input^0 will ALWAYS be 1 and it's actually 
x^y = 1 * input * input * input * input, meaning that input1 for first i 
is accounted for. 
"""


# PROBLEM 2

import math
def minandmax(list1):
   max_val = max(list1)
   min_val = min(list1)
   tupleminmax = (min_val, max_val)
   print(tupleminmax)
   return [tupleminmax]


# PROBLEM 3

def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return False
    else: 
        return False


# PROBLEM 4

def calculate_bmi(weight, height):
    return weight / (height ** 2)


# PROBLEM 5

def rotate_digits(digits):
    last_digit = digits % 10
    first_digits = digits // 10
    print(f"{last_digit}{first_digits}")
    return [f"{last_digit}{first_digits}"]


# PROBLEM 6: Maximum

list1 = [1, 3, 5, 7, 4, 6]

# as a for function
def findMax(lis):
    max1 = lis[0]
    for x in range(len(lis)):
        num = lis[x]
        if num > max1:
            max1 = num
    return max1 #don't use brackets unless want return to be a list!

# as a while function
def whilefindMax(lis):
    max1 = lis[0]
    x = 0
    while x < len(lis):
        num = lis[x]
        if num > max1:
            max1 = num
        x = x + 1
    return max1


# PROBLEM 7: Minimum

# as a for function
def findMin(lis):
    min1 = lis[0]
    for x in range(len(lis)):
        num = lis[x]
        if num < min1:
            min1 = num
    return min1

# as a while function
def whilefindMin(lis):
    min1 = lis[0]
    x = 0
    while x < len(lis):
        num = lis[x]
        if num < min1:
            min1 = num
        x = x + 1
    return min1


# PROBLEM 8

# as a for function
def product(numList):
    input1 = numList[0]
    for i in range((len(numList))):
        input = numList[i]
        input1 = input1 * input
    print(input1)
    return [input1]

#as a while function
def whileProduct(numList):
    input1 = numList[0]
    x = 0
    while x < len(numList):
        input = numList[x]
        input1 = input1 * input
        x = x + 1
    print(input1)
    return input1


# PROBLEM 9

"""
For both functions, it is assumed that all input strings include only lowercase letters!
Mainly because it would be more of the same of what was done for the lowercase vowels,
just with uppercase letters. 
"""

# as a for function
def countVowels(str):
    for x in range(len(str)):
        a = str.count("a")
        i = str.count("i")
        e = str.count("e")
        o = str.count("o")
        u = str.count("u")
    return [f"The number of vowels is {a + e + i + o + u}"]

# as a while function
def whilecountVowels(str):
    vowelcount = 0
    x = 0
    while x < len(str):
        letter = str[x]
        if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
            vowelcount = vowelcount + 1
        x = x + 1
    return [f"The number of vowels is {vowelcount}"]


# PROBLEM 10

def sumDigits(num):
    x = 0
    total = 0
    strnum = str(num)
    while x < len(strnum):
        digit = strnum[x]
        total = total + int(digit)
        x = x + 1
    return [f"the digital root is {total}"]