#3 Lists
#3.1 List Operations

fav_food=["apple", "pear", "orange", "raspberry", "mango"]
print(fav_food[1]) #print second element
print(fav_food[-1]) #print last element with negative indexing
fav_food.append("ananas") #appending new fruit

"""I encountered this error: 
TypeError: insert expected 2 arguments, got 1
I wrote: fav_food.insert("apple"). The problem is that the index of the element to be inserted is missing
I fixed it by plugging in the index: fav_food.insert(0, "apple")"""

fav_food.insert(0, "apple") #inserting apple at teh start of the list
#print(fav_food) 

fav_food.pop(2) #removing the third item
print(len(fav_food)) #printing the elements

for i in fav_food: print(i.upper())
#for i in range(len(fav_food)): print(fav_food[i].upper())

food_new = fav_food[::5] #creating a new list containing on the first and the last element by striding

#check whether a certain string is contained in the list
if food_new == "Potato":
    print("A potato!")
else: 
    print("No potato!")

#3.2 Slicing and Striding
numbers=list(range(21))

def get_first_15(numbers):
   return numbers[:15] #from element with index zero to element with index 14 = first 15 elments

def get_every_5th(lst):
    return lst[::5] #returns every 5th element

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


"""Here, I made a logical mistake first. I wanted to put the following 3 lists into one list.
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
But this would not have worked because this would have given me a longer list with 3 list elements in one dimension
and not a matrix with 2 dimensions.
"""

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(range(len(numbers)))

"""
Checking the correctness of the logical error above. printing numbers gives a one dimensional list with three elements and not a matrix
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
    l = [ #creat a list with zeros only in 5 rows and 5 columns
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    counter=1 #setting a counter to fill the list
    for rows in range(5): #iterating over rows with index 0 to 4
        for columns in range(5):  #iterating over columns in each row
            l[rows][columns]=counter #filling each cell with the counter value
            counter+=1 #increase the counter value by one
    return l



#1. Write a function that replaces all multiples of 3 with “?”. Store the updated 5x5 list in anew variable.
def replace(l):
    #range(len(l)) gives the indices of the rows of the nested list
    for row in range(len(l)):
        for column in range(len(l[row])): #range(len(l[0])) gives the indices of the columns of the first row
            if l[row][column]%3==0: #if cell value is divisble by 3 replace the cell value with a ?
                l[row][column]="?"
    return l

m=list_create()
r= replace(m)
#print(r)

#2. Write a function that adds all elements not equal to “?” and returns the sum. Save the result in a variable.Hint: Use != to skip “?”.
#Note: To clarify, edit the list with the first function and then edit it again with the second function.
def total_sum(l):
    total=0 #define a counter for the total sum
    for row in range(len(l)): #iteratate over rows in l. 
        for column in range(len(l[row])): #iterate over the columns of each row
            if l[row][column]!="?": #if a cell value is unequal to a question mark, increase the total sum with the cell's value
                total+=l[row][column]
    return total

#t= total_sum(r)
#print(t)


#4 dictionaries
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

#1.Print “Katie”’s age.
print(ages["Katie"])
"""
I encountered this error
   KeyError: 1
   I wrote: Print(ages[1]). The error was that I cannot access the value of the first key by calling the dictionary and index element with index 1
   I corrected it by writing print(ages["Katie"]), so, I wrote tha name of the key whose value I want to print out.
"""


#2. change mira's age to 100
ages["Mira"]=100
#print(ages)

# Add ‘‘Milana" with an age of 52.
ages["Milana"]=52

del ages["Mariam"]
"""
I received this error: SyntaxError: cannot delete function call
I wrote: del ages(2)
I corrected that by writing: del ages["Mariam"]. My mistake was first that I didnt use edgy brackets and second that I nted to index a key instead of writing the key.
"""

#print(ages)

for key, value in ages.items():
    print(f"{key}, {value}")

r = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]

print(total_sum(r))


