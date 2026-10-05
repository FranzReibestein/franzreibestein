# 3. print functions

#3.1 say goodbye
def say_goodbye(name):
    #print goodbye and the name argument
    print("Goodbye", name)

#3.2 area of a circle
def circle_area(radius):
    #print area of the circle with approximated formula for pi
    print("The area of the circle equals", 3.14**2*radius)
#4 return functions

#4.1 subtract, multipy, and devide
def subtract(a, b): 
    #return the difference
    return a - b

#print(subtract(20, 25))

def multiply(a,b): 
    #return the product
    return a*b

def divide(a,b): 
    #return the quotient
    return a/b

#5- conditions
#5.1 What Should I Wear?
def what_to_wear(temperatures):
    #extract the highest and lowwest temperature and put them into a tuple
    min_max_temp = (min(temperatures), max(temperatures))
    #return the tuple
    return min_max_temp

#5.2 Check if it’s the Weekend

def is_weekend(day):
    #require to type in a weekday
    if day < 1 or day > 7:
        return "Type in a valid weekday"
    #condition for a weekday
    elif day >= 1 and day <= 5:
        return False
    else: 
        return True

# 5.3 Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel_used):
    #create an empty list
    efficiency = []
    #calculate the fuel efficiency for every car and save this value in the created list
    for i in range(len(distance)):
        efficiency.append(fuel_used[i] / distance[i])
    #return the list
    return efficiency

#5.4 Secret Code
def secret_code(number): 
    #calculate the encrypted number: the last digit is the original number mod 10. the rest of the original number is number // 10
    #idea: we have to find out how many digits we have in the whole number
    rest=number//10 #we will add this rest to our final encrypted number
    y=number//10 #this is a auxiliary varaible to find out how many digits we have
    last_digit=number % 10 #this will be the leading digit of our original number
    i=10 #this will be the factor of our leading digit. as our rest is already number mod 10, we have to multiply the leading digit at leat with 10
    while y //10 >0: #as long as the rest integer divided by 10 >0 we have at least one more digit left, thus we have to multiply the factor of the leading digit with 10
        i*=10
        y//=10
    return i*last_digit+rest


#6 Loops
#6.1 Oski Stole Your Power
def power_function(base, exponent):
    #define a power varaible and set it to one
    power = 1
    #change the value of the power variable by iterratively multiplying the base with itselfes (exponent-many times)
    for i in range(exponent):
        power *= base
    return power

#6.2 Min & Max with Loops!
#6.2.1 For Loops

def find_min(numbers):
    #use the element with index 0 as the starting minimun
    min_value = numbers[0]
    #iterate over the list and compare whether the recent element is smaller than the recent smallest element. If so, it becomes the new smallest element.
    for i in range(len(numbers)):
        if numbers[i]<min_value:
            min_value = numbers[i]
    return min_value

def find_max(numbers):
    #use the element with index 0 as the starting maximum
    max_value = numbers[0]
    #iterate over the list and compare whether the recent element is bigger than the recent biggest element. If so, it becomes the new biggest element.
    for i in range(len(numbers)):
        if numbers[i]>max_value:
            max_value = numbers[i]
    return max_value

#6.2.2 While Loops
#min
def minimum(numbers):
    #define an index and use the element with index 0 as the starting minimun
    i = 0
    minimum = numbers[0]
    #loop as long our index i is smaller than the highest index value of our input list
    while i <= len(numbers)-1:
        #the recent number becomes the new smallest element, if it is smaller than the recent smallest element
        if numbers[i]<minimum: minimum = numbers[i]
        #increase the index by one after each iteration of the loop
        i +=1
    return minimum

def maximum(numbers):
    #define an index and use the element with index 0 as the starting maximum
    i = 0 
    maximum = numbers[0]
    #iterate as long as our running index is smaller than or equal to the index of the last element in the input list
    while i <= len(numbers)-1:
        #if the recent element is bigger than the recent biggest element, it becomes the new biggest element
        if numbers[i] > maximum: maximum = numbers[i] 
        #increase the running index after each loop iteration by 1
        i+=1
    return maximum

#print(maximum([10,20,30,40]))

#6.3. calculate the sum
def digit_sum(number):
    #we define the local variables x and sum_of_digits. sum_of_digits will become the sum of the digits and has initial value 0. 
    # x is an auxiliary variable which is equal to the absolut value of the input integer. We take the absolute value because
    #the sum of the digits of -12 is equal to the sum of the digits of 12.
    x = abs(number)
    sum_of_digits = 0
    #iterate as long x is bigger than zero.
    while x > 0: 
        #increase the digit sum by the mod of x integer divided by 10
        sum_of_digits += x % 10
        #Drop the last digit of the recent number. So, we can access its recent penultimate digit in the next iteration
        x //= 10
    return sum_of_digits

x = 2468
result = digit_sum(x)

print(f"The sum of the digits of the integer {x} equals {result}.")





       
        







