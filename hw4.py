#Q2 PART 3

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

listC = []
for i in range (len(listA)):
    mynum = listA[i]
    if (mynum % 2) == 1:
        listC.append(mynum)
print(listC)
for i in range(len(listB)):
    mynumm = listB[i]
    if (mynumm % 2) == 1:
        listC.append(mynumm)
print(listC)

""""
Error 1: Terminal reported invalid syntax for line 1 yet there were no errors 
in line 1 because it was copied from the homework template. Resolved
by trashing every terminal and reopening a new terminal. 
Error 2: Invalid syntax because I put a period in my variable name; resolved by
removing the period from the variable name. 
Error 3: Terminal repeatedly listed massive amounts of errors. Resolved by 
completing work in a separate python file to avoid dealing with errors from 
template. 
"""

#Q3 PART 1

list_2D = []
for i in range(0,5):
    listh = []
    for ii in range(1,6):
        ii = ii + 5 * i
        listh.append(ii)
    list_2D.append(listh)
print(list_2D)


#Q3 PART 2
# can also index around list_2D instead of trying to remake it!! (But I did not do that.)

list_2D2 = []
for i in range(0,5):
    listg = []
    for ii in range (1,6):
        ii = ii + 5 * i
        if (ii % 3) == 0:
            listg.append("?")
        else: 
            listg.append(ii)
    list_2D2.append(listg)
print(list_2D2)


"""
Error 1: Terminal reported invalid syntax and did not 
provide any further feedback. Resolved by trashing every terminal 
and reopening a new terminal. 
Error 2: Invalid syntax message for line 20. Resolved by adding 
quotation marks around "?".
"""

#Q2 PART 1

list050 = []
for i in range(0, 51):
    list050.append(i)
print(list050)


"""
Error 1: Printed a list of the 50 copies of the number 0. 
Resolved by putting list050.append(i) instead of list050.append(0). 
Error 2: Did not print. Resolved by adding print(list050) to the 
end of the code. 
"""

#Q2 PART 2

list0502 = []
for i in range (len(list050)):
    ii = i**2
    list0502.append(ii)
print(list0502)


"""
Error 3: Printed 50 lists, each with the square of the term 
corresponding the i of the list. 
Resolved by removing indentation from print(list050). 
"""

#Q4

def remove_duplicates(a):
    seen = set()
    seen_add = seen.add
    copya = [x for x in a if not (x in seen or seen_add(x))]
    print(copya)
    return [copya]

test = [80, 40, 10, 80, 50, 40, 20, 60, 30, 80]
remove_duplicates(test)


"""
Error 1: Invalid syntax in line with return command. 
Resolved by indenting the code so that return was within 
the function defined.
Error 2: Invalid syntax within brackets of return command. 
Seen was considered invalid syntax because it was not also 
preceded by the word "in." 
Error 3: Used copya.append instead of just setting 
seen_add = seen.add so that copya is just all of the x 
that aren't duplicates, automatically in the same order. 
Error 4: Did not recognize seen or seen_add(x) for definition 
of copya even though they had been defined in the function 
in the two lines just above. Resolved by removing the extra 
indentation of the lines where seen and seen_add(x) were 
introduced, so that their indentation was the same as that of 
the definition of copya. 
"""