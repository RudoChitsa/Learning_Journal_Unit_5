#1. Consider the loop from Section 8.3 of your textbook.

#prefixes = 'JKLMNOPQ'
#suffix = 'ack'

#for letter in prefixes:
#     print(letter + suffix)

#Put this code into a Python script and run it. Notice that it prints the names "Oack" and "Qack".

#Modify the program so that it prints "Ouack" and "Quack" but leaves the other names the same.

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
        if letter in ('O', 'Q'): 
            print (letter + 'u' + suffix)
        else:
            print (letter + suffix)

___________________________________________________________________________________________
#Using Indexing Operator
#The indexing operator [Python uses square brackets to enclose the index]
subject = "Programming"
s = subject[5]
print(s)

#OUTPUT
a
>>>
___________________________________________________________________________________________
#Using Length
#The len function returns the number of characters in a string

long_word = "Hippopotamus"
len(long_word)

#OUTPUT
12
>>>
___________________________________________________________________________________________
#Using Substring
#A substring of a string is obtained by taking a slice.

subjects = ["English", "Maths", "Science", "Computer_Science", "Geography", "History", "Accounting"]
>>> print(subjects[3:5])

#OUTPUT
['Computer_Science', 'Geography']
>>>
____________________________________________________________________________________________