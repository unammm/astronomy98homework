# PROBLEM 1
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

# PROBLEM 2
"""
import math
def minandmax(list1):
   max_val = max(list1)
   min_val = min(list1)
   tupleminmax = (min_val, max_val)
   print(tupleminmax)
   return [tupleminmax]
"""

# PROBLEM 3  FIX!!
"""
def leapYear(year):
    if year % 4 == year / 4: 
        if year % 400 == year / 400: 
            if year % 100 == year / 100:
                print("True")
                return ["True"]
            else: 
                print("False")
                return ["False"]

leapYear(2024)
"""

# PROBLEM 4
"""
def calculate_bmi(weight, height):
    return weight / (height ** 2)
"""

# PROBLEM 5 
"""
def rotate_digits(digits):
    last_digit = digits % 10
    first_digits = digits // 10
    print(f"{last_digit}{first_digits}")
    return [f"{last_digit}{first_digits}"]
"""

### For questions #6-10, write the solution with a for-loop and a while-loop.
# If it is not possible to write it with a for-loop or while-loop, detail why.

# PROBLEM 6 FIX!!!
"""
list1 = [1, 3, 5, 7, 4, 6]

def findMax(lis):
    for x in range(len(lis)):
        seen = set()
        while x > seen:
            max = x
            print(f"{x for x > seen}")
            return [x for x > seen]
        
findMax(list1)
"""

# PROBLEM 7 FIX !!!
"""
list1 = [1, 3, 5, 7, 4, 6]
def findMin(lis):
    for x in range(len(lis)):
        seen = set()
        seen_add = seen.add()
        while x < ( x in seen or seen.add(x)):
            min = [x for x in lis if ( x < seen or seen.add(x))]
            print(min)
            return [min]
        
findMin(list1)
"""

# PROBLEM 8 FIX!!!
"""
def product(numList):
    input = numList[i]
    for i in range(numList):
        input = input * input
    print(input)
    return [input]

list = [ 1, 2, 3]
product(list)
"""


# PROBLEM 9 FIX!!!!
"""
string1 = "pneumonoultramicroscopicsilicovolcanoconiosis"

def countVowels(str):
"""
# PROBLEM 10 FIX!!!
"""
def sumDigits(num):
    input1 = num[i]
    for i in range(len(num)):
        input1 = input1 + input
    print(input1)
    return[input1]

list1 = [1, 2, 3]
sumDigits(list1)
"""