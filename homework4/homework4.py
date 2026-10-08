#3 Lists
#3.1 List Operations

fav_food=["apple", "pear", "orange", "raspberry", "mango"]
print(fav_food[1])
fav_food.append("ananas")
fav_food.insert(0, "apple")
print(fav_food)

fav_food.remove("pear")
print(len(fav_food))

for i in fav_food: print(i.upper())
for i in range(len(fav_food)): print(fav_food[i].upper())

print(fav_food)

food_new = fav_food[::5]
print(food_new)

#check whether a certain string is contained in the list
if food_new == "Potato":
    print("A potato!")
else: 
    print("No potato!")

#3.2 Slicing and Striding
numbers=list(range(21))

def get_first_15(numbers):
   return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]
#if i do not define start and stop, start and stop depend on the sign of step. if step has a negative sign, the last element is the starting element.

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1, step2, step3)

#3.3 Nested Lists
#3.3.1 Nested List Operations

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(range(len(numbers)))

"""
numbers2 = [list_1, list_2, list_3]
print(numbers2)
print(numbers)
"""
#print 3rd row
print(numbers[2])

# Print the second item in the second row.
print(numbers[1][1])

#3. Add [10, 11, 12] as a new row using .append().
numbers.append([10,11,12])

#4. Write a function called sum nested() that loops through each row, sums all numbers, and returns the total.
def sum_nested(n):
    sum=0
    for row in n: #iterate over rows
        for column in row: #iterate over the columns in a row
            sum+=column  
    return sum

print(sum_nested(numbers))

#3.4 Create a 5x5 List
#Write a function that uses nested for loops to create a 5x5 list of numbers from 1 to 25. Store the result in a new variable.
def list_create():
    l = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    counter=1
    for rows in range(5):
        for columns in range(5): 
            l[rows][columns]=counter
            counter+=1
    return l

m = list_create()
print(range(len(m)))
print(range(len(m[0])))
print(m)



#1. Write a function that replaces all multiples of 3 with “?”. Store the updated 5x5 list in anew variable.
def replace(l):
    #range(len(l)) gives the indices of the rows of the nested list
    for row in range(len(l)):
        for column in range(len(l[row])): #range(len(l[0])) gives the indices of the columns of the first row
            if l[row][column]%3==0: 
                l[row][column]="?"
    return l

r= replace(m)
print(r)

#2. Write a function that adds all elements not equal to “?” and returns the sum. Save the result in a variable.Hint: Use != to skip “?”.
#Note: To clarify, edit the list with the first function and then edit it again with the second function.
def total_sum(l):
    total=0
    for row in range(len(l)):
        for column in range(len(l[row])):
            if l[row][column]!="?":
                total+=l[row][column]
    return total

t= total_sum(r)
print(t)

""" I want to check whether I can write a function that does the same in another way
def total_sum2(r):
    total=0
    for row in r:
        for column in row:
            total+=column
    return total

r=list_create()

print(r)
print(total_sum2(r))

"""


#4 dictionaries
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

#1.Print “Katie”’s age.
print(ages["Katie"])

#2. change mira's age to 100
ages["Mira"]=100
print(ages)

# Add ‘‘Milana" with an age of 52.
ages["Milana"]=52

del ages["Mariam"]

print(ages)

"""
for key, value in ages.items():
    print(f"{key} is {value} years old.")

for key in ages:
    print(key)

for value in ages.values():
    print(value)
"""



