# PROBLEM 1 good
"""
def power(input, power):
    input1 = 1
    for i in range(power):
        input1 = input1 * input
    print(input1)
    return [input1]
"""
"""
input1 or input' = 1 since input^0 will ALWAYS be 1 and it's actually 
x^y = 1 * input * input * input * input, meaning that input1 for first i 
is accounted for. 
"""

# PROBLEM 2 good
"""
import math
def minandmax(list1):
   max_val = max(list1)
   min_val = min(list1)
   tupleminmax = (min_val, max_val)
   print(tupleminmax)
   return [tupleminmax]
"""


# PROBLEM 3 good
"""
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return False
    else: 
        return False
"""


# PROBLEM 4 good
"""
def calculate_bmi(weight, height):
    return weight / (height ** 2)
"""

# PROBLEM 5 good
"""
def rotate_digits(digits):
    last_digit = digits % 10
    first_digits = digits // 10
    print(f"{last_digit}{first_digits}")
    return [f"{last_digit}{first_digits}"]
"""


### For questions #6-10, write the solution with a for-loop and a while-loop.
# If it is not possible to write it with a for-loop or while-loop, detail why.

# PROBLEM 6: Maximum good
"""
list1 = [1, 3, 5, 7, 4, 6]

def findMax(lis):
    max1 = lis[0]
    for x in range(len(lis)):
        num = lis[x]
        if num > max1:
            max1 = num
    return max1 #don't use brackets unless want return to be a list!

findMax(list1)
"""
"""
def whilefindMax(lis):
    max1 = lis[0]
    x = 0
    while x < len(lis):
        num = lis[x]
        if num > max1:
            x = x + 1
            max1 = num
    return max1
"""

# PROBLEM 7: Minimum good
"""
def findMin(lis):
    min1 = lis[0]
    for x in range(len(lis)):
        num = lis[x]
        if num < min1:
            min1 = num
    return min1
"""

"""
def whilefindMin(lis):
    min1 = lis[0]
    x = 0
    while x < len(lis):
        num = lis[x]
        if num < min1:
            x = x + 1
            min1 = num
    return min1
"""

# PROBLEM 8 good
"""
def product(numList):
    input1 = numList[0]
    for i in range((len(numList))):
        input = numList[i]
        input1 = input1 * input
    print(input1)
    return [input1]
"""
def whileProduct(numList):
    input1 = numList[0]
    x = 0
    while x < len(numList):
        input = numList[x]
        input1 = input1 * input
    print(input1)
    return input1

List = [ 1, 2, 3, 4 ]

whileProduct(List)


# PROBLEM 9 good
"""
string1 = "pneumonoultramicroscopicsilicovolcanoconiosis"

def countVowels(str):
    for x in range(len(str)):
        a = str.count("a")
        i = str.count("i")
        e = str.count("e")
        o = str.count("o")
        u = str.count("u")
    return [f"The number of vowels is {a + e + i + o + u}"]
"""



# PROBLEM 10 good
"""
def sumDigits(num):
    input1 = 0
    for i in range(len(num)):
        input = num[i]
        input1 = input1 + input
    print(input1)
    return[input1]
"""