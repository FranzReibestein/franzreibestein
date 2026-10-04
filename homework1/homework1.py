# File: homework1.py

# ---3.1 Variables and Data Types ---
a=10
print(a)
print(type(a))
print(a, "is an integer, a whole number with no decimals")

b=1.5
print(b)
print(type(b))
print(b, "is a float, a number with decimals")

c=3j
print(c)
print(type(c))
print(c, "is a complex number, a number with a real and an imaginary part")

d="hello"
print(d)
print(type(d))
print(d, "is a string, a sequence of characters enclosed in quotation marks")

e = [1, 2, 3]
print(e)
print(type(e))
print(e, "is a list, an ordered collection of items. The items in a list can be of different data types and can be modified via indexing. e is a list of integers.")

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
print(f, "is a dictionary, an unordered collection of key-value pairs. The values can be altered by using the keys.")

g = (1, 2)
print(g)
print(type(g))
print(g, "is a tuple, an ordered collection of items. The items in a tuple can be of different data types but cannot be modified once the tuple is created.")

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
print(h, "is a list, an ordered collection of items which can be altered via indexing.")

i = True
print(i)
print(type(i))
print(i, "is a boolean, a data type that can only have two values: True or False.")

j = None
print(j)
print(type(j))
print(j, "is a NoneType, a data type that represents a single value, i.e. no value available.")

k = [True, "blue", 12]
print(k)
print(type(k))
print(k, "is a list containing 3 different data types: Boolean, string, and integer.")

l = str(14)
print(l)
print(type(l))
print(l, "is a string, a sequence of characters enclosed in quotation marks.")

m = 1e4
print(m)
print(type(m))
print(m, "is a float, a number with decimals.")

# Answers to the questions in 3.1
#3.1.1 I found 9 different data types.

#3.1.2 integer, float, complex, string, list, dictionary, tuple, boolean, and NoneType.

#3.1.3 Variables of the same data type
#float: b, m
#list: e, h, k
#string: d, l

#3.1.4 What was the data type of l? Why is it not an integer? What does str() do?
"""
str() is a function that converts the data type of the variable inside the brackets into a string. Therefore, l is of data type string, because the string
function converts the data type of the integer 14 to a string.
"""

#3.1.5
n={1,1,4,3,2,2,3}
print(n)
print(type(n))
print(n, "is a set, an unordered collection of unique items.")

# ---3.2 Booleans ---
print(10 > 9) #True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True- The input of teh bool function is the string abc.
#help(bool)
print(bool(123)) #True. The input of the bool function is the integer 123.
print(bool(["apple", "cherry", "banana"])) #True. The input of the bool function is a list containing three strings.
print(bool(True)) #True. The input of the bool function is the boolean value True.

print(bool(False)) #False. The input of the bool function is the boolean value False.
print(bool(0)) #False. The input of the bool function is the integer 0.
print(bool("")) #False. The argument is an empty string.
print(bool(" ")) #True. The argument is a string only including a dash. 

print(bool(())) #False. The input of the bool function is an empty tuple.
print(bool([])) #False. The input is an empty list.
print(bool({})) # False. The input is an empty dictionary.

print(bool(True and False)) #False. The inputs are the boolean values True and False, connected via the operator and.
print(bool(True and True)) #True. The inputs are the boolean values True and True, connected via the operator and.
print(bool(False and False)) #False. The inputs are the boolean values False and False, connected via the operator and.
print(bool(True or False)) #True. The inputs are the boolean values True and False, connected via the operator or.

print(bool(True or True)) #True. The inputs are the boolean values True and True, connected via the operator or.
print(bool(False or False)) #False. The inputs are the boolean values False and False, connected via the operator or.
print(bool(not(False))) #True. The input of the boolean function is a negation of the boolean value False, which is True.
print(bool(not(True))) #False. The input of the boolean function is a negation of the boolean value True, which is False.

#Questions for 3.2
#What pattern do you notice about expressions returning True or False?

"""
I noticed that untrue expressions returned false, like print(10==9), while true expressions (like print(10==10)) returned True.
Furthermore, I noticed that the boolean function returned True for non-empty inputs as well as the boolean value True, and False for empty inputs as well as 
the boolean value False. Finally, I noticed that the boolean Function returns True when at least one of two statements, which are connected via the or operator, 
is true, and returns True for two true statements connected via the and operator.
"""

#Which expression surprised you about its result?
#I was surprised that bool(0) returned False, because 0 is an integer, and for the integer 123, bool(123) returned True.

#Create an expression, not given above, that will return True. Why is it True?
print(bool(1.6)) #True because the input of the boolean function is a float.

#Create an expression, not given above, that will return False. Why is it False?
print(bool(0.0)) #False because the input of the boolean function is float with value 0.0.
#It seems as if the boolean function would return True for integer and float values unequal to zero, and False for integer and float values equal to zero.

# ---3.3.1 Arithmetic Operators ---
print(10 + 5) #15, + performs addition.
print(10 - 5) #5, - perfroms subtraction.
print(2 * 4) # 8, * perfroms multiplication.
print(6 / 3) # 2, / performs division.
print(5 % 2) # 1, % performs modulus, which returns the remainder of a division.
print(3 ** 2) # 9, ** raises three to the power of 2.
print(15 // 2) #7, // performs floor division, which returns the largest integer less or equal to the quotient of a division.

# ---3.3.2 Comparison Operators ---
print(5 == 2) # False. == checks wheter two values are equal.
print(10 != 10) #False. != checks whether two values are unequal. 10 is not unequal to 10.
print(2 < 5) # True. < checks wheterh the first value is smaller than the second value. 2 is smaller than 5.
print(12 > 5) # True. > checks whether the first value is greater than the second value. 12 is grater than 12.
print(5 <= 6) # True. <= checks whether the first value is smaller than or equal to the second value. 5 is smaller than 6.
print(1 >= 10) # False. >= checks whether the first value is greater than or equal to the second value. 1 is smaller than 10.

# ---3.3.3 Assignment Operators ---
x=5
x += 5
print(x) #10. += adds the value on the right to the variable on the left and assigns the result to the variable on the left.
x -= 4
print(x) #6. -= subtracts the right value from the varaible on the left and assigns the result to the varaible on the left.
x *= 3
print(x) #18. *= multiplies the variable on the left by the value on the right and assigns the result to the varaible on the left.

# ---3.3.4 Logical Operators ---

#1. The operator and relates two statements and retruns True if both are correct and returns False if less than two are correct.
print(10==9 and 5==5) #False.

#2. The or operator relates two statements and retuns True if at least one of them is correct and returns False if both are incorrect.
print(10==9 or 5>90) #False.

# The not operator negates a statement and returns True if a statement is False and returns False if a statement is true.
print(not(5>3)) #False

#More Questions

#1. / calculates the quotient of a division, so it can yield a float (i.e. decimal) number. // performs floow division, i.e. it can only return integers.

#2. % returns the remainder of a division, whereas // (floor division) returns the largest integer less or equal to the quotient resutling from a division.

#3. To calculate the remainder, I would use the % operator. I want to know the remainder of dividing 7 by 3, which is one.

z=7%3
print(z) #1

#4. How do assignment operators work. See my comments in 3.3.3. Generally, they perform a specified mathematical operation with a variable and assign the result 
# to the variable.


# ---3.4 Strings---
my_string = "hello"
print(my_string) # Prints: hello

print(my_string[0]) #prints: h
print(my_string[1]) #prints: e
print(my_string[2]) #prints: l
print(my_string[3]) #prints: l
print(my_string[4]) #prints: o
print(my_string[-1]) #prints: o
print(my_string[1:3]) # prints: el #the last index 3 is not included
print(my_string[0:5:2]) #prints: hlo (from index 0 to index 4(included) and cut out every second word)
print(len(my_string)) #5

print(my_string + "goodbye") #hellogoodbye

print(7*my_string) #hellohellohellohellohellohellohello

# ---3.4.1 Questions---
"""
1. Slicing refers to the extraction of a subsequence from an ordered sequence via the so called [start:stop:step notation].
Start refers to the index of the original sequence; the slice, or subsequence, starts with the element that corresponds to that index. 
The stop index is not included in the slice, so if stop is 5, the slice ends at the element with index 4 of the original sequence.
Finally, step refers to the frequence of elements to be extracted. step=1 means to extract every element, step=2 means extracting every second element, 
and so on.
Slicing was applied in 8 and 9.
"""

#2.
name = "Oski"
print("Hello, my name is", name)
#Hello, my name is Oski

#3.
name = "Oski"
print(f"Hello, my name is {name}")
#Hello, my name is Oski

#4. 
"""
The code output is the same, but clearly, the code input is different. In 2), I plugged in
2 different arguments into the print function, the string "Hello, my name is" and the value of 
the variable name. The print function automatically inserts a space between the words is and the value of name.
In 3), we plug only one string argument into the print function. The f in the parantheses tells the print function
that the string argument is an f-string, which means that {name} is only a place holder of a value
that was already assigned to name. Furthermore, in 3), we have to type the space between is and {name} which we had not to do in 2).
"""

# ---3.5 Terminal Commands---
"""
cd
Changes directories. Use it to move from one folder to another
Example: cd somefoldername/astro98/myname/hw1

ls
shows the non-hidden files and subfolders of a folder
exampe: ls C:/Users/franz/Astro98

ls -a (a for all) shows all the files and subfolders of a folder, e.g. also hidden files/folders or folders/files whose name starts with a .
example: ls -a C:/Users/franz/Astro98

mkdir
Creates a directory in the recent working directory
example: mkdir hw1

cat
prints all the contents of a text file to the terminal without executing them
Ex: cat datatypes.py

pwd
Prints the path to the current working directory
Ex. pwd #/c/Users/franz/Astro98

cd ..
change the working directory from the current working directory to its parent directory
ex: cd..#/c/Users/franz

cd .
woking directory remains the same
ex. cd ./c/Users/franz

cd ~
no matter what my working directory is, cd ~ changes my working directory to my home directory


cp 
creates a copy of a file or folder in the recent working directroy and copies it into a folder to be specified
ex. cp datatypes.py /c/Users/franz

mv
with the move command, I can move and/or rename files
Ex: mv text.txt test.txt

rm
This command removes a file.
Ex. rm test.txt

clear
Deletes all inputs and outputs from the console of my terminal.
Ex. clear

grep
This command shows all lines of a file that match a search term.
Ex. grep "print" homework1.py
"""


#---Questions:---
"""
1. Look up 3 other commands not present. Define and explain how to use them on the command
line.

nano
With this command, I can edit text files via the terminal.
Ex. nano datatypes.py

rmdir
Removal of a directory
Ex. rmdir bier

touch
Creation of a file.
Ex. touch test.txt

2. What is the difference between ls and ls -a?
ls only lists normal, non-hidden files and subfolders of a folder. ls -a lists all subfolders and files of a given folder including hidden files and subfolders.

3. What is a hidden file?
A hidden file is a file whose name begins with a dot.


4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
use them on the command line.

grep -i
This command shows all lines of a file that match a search term in a non-case-sensitive way.
Ex. grep -i "print" datatypes.py

ls -l
Lists the unhidden subfolders and files of a folders, but other than ls, it shows additional details for each file/folder, like last modification date, owner, size.
Ex. ls -l /c/Users/franz

rm -r
Removes a folder with all the files and subfolders it contains
Ex. rm -r DemoClass2

"""

