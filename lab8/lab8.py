"""
student's  full name
April 20, instrouction  python
"""
# Single comment. This line WILL NOT run
print('\n ----- Example 1:  string characters -----')
print("\tGood morning! \nThis is  my first \"Python\" code!")

print('\n  -----example 2: data type -----')
print(f"Data type of 3.56 = {type(3.56)}")   # f is place holder
print(f"Data type of -25 = {type(-25)}")
print(f"Data type of 'Hello World!'  = {type('Hello World!')}")
print(f"Data type of  character '$' = {type('$')}")
print(f"Data type of False = {type(False)}")


print('\n ----- Example 3:variables -----')
# Declare variables
number1 = 25.5
number2 = -12
username = "Peter Pan"
add_numbers = number1 + number2
is_raining = True

# Prompt results
print(f"{username}, the sum of {number1} and {number2} is {add_numbers}")
print(f"  Is it raining today ? = {is_raining}")


print('\n-----Example 4: assigning values to multiple variables -----')
#  Declare miltiple variables
item1,  item2, item3 = "apples", 25, False
print(f"item1 = {item1},  item 2 = {item2}, item3 = {item3}")
# Declare miultiple varaibles with the same values
score1 = score2 = score3 = 99
print(f"score 1 = {score1}, score 2 = {score2}, score 3 = {score3}")
      
print('\n-----Example 5: input command -----')
print("Enter username: ")
username = input()
print(f"Collected  username = {username}")


# Cast from string to integer
print("Enter a lucky number: ") #can be removed to below.
luckynumber = int(input("Enter a lucky number:")) #instead of above print statement.
print(f"Lucky number = {luckynumber}")

# Double the lucky number. Cast from string to integer.
dblucky = int(luckynumber)*2
print(f"Doubled of lucky = {dblucky}")

# Cast integer(or float) in to string
triplenumber = str(dblucky) * 3   
print(f"tripled the casted number = {triplenumber}")

# Cast integer to bool value
# 0 is false, any another number is true. in Python.
completed_task = -20 
print(f"completed task = {bool(completed_task)}")

print('\n-----Example 6: arithmetic operators -----')
num1 = 5
num2 = 9

print(f"The sum of {num1} and {num2} is                       {num1 + num2}")
print(f"The different between {num1} and {num2} is            {num1 - num2}")
print(f"The product of {num1} and {num2} is                   {num1 * num2}")
print(f"The quotient of {num1} and {num2} is                  {num1 / num2}")
print(f"The floor division of {num1} and {num2} is            {num1 // num2}")
print(f"The modulous (remainder) of {num1} and {num2} is      {num1 % num2}")
print(f"The integer of quatioen of {num1} and {num2} is       {num1 // num2}")
print(f"The result of base {num2} to the power of 3 is        {num2 **3}")

print('\n-----Example 7:  arithmetic operators -----')
# Declare and assign values to variables.
x =  float(input("Enter side 1: "))
y  =  float(input("Enter side 2: "))
# Calculate the hypotenuse
hyp =   (x**2 + y**2)**0.5
# Prompt the result
print(f"The hypotenuse of {x : 0.1f} and {y : 0.1f} is {hyp: 5.2f}") #  5 is the total number of digits, 2 is the number of decimal places.
# The result is rounded to 2 decimal places.

print('\n-----Example 8: assignment operators -----')
n = 20
print(f"number =           {n}")
# Assignment operators  +
n += 3
print(f"number +3 =        {n}") #  This is the same as n = n + 3.
n -= 4
print(f"updated - number = {n}") #  This is the same as n = n - 4.
n *=  2
print(f"updated * number = {n}") #  This is the same as n = n * 2.
n /= 3
print(f"updated / number = {n}") #  This is the same as n = n / 3.
n //= 2
print(f"updated // number = {n}") #  This is the same as n = n // 2.
n -= 4
print(f"updated - number = {n}") #  This is the same as n = n - 4.

# Modulus or remainder operator
n  %= 5
print(f"updated %= number = {n}") #  This is the same as n = n - 4.

print('\n-----Example 9: comparison operators -----')
n1 = 10
n2 = 3
n3 = 7
compare1 = n1 == n2
compare2 = n1 == (n2+n3)
print(f"is n1 equal n2?                 {compare1}") 
print(f"is n1 equal to n2 + n3?         {compare2}")
compare3 = n1 > n2
compare4 = n2 <= n3
print(f"is n1 greater than n2?          {compare3}")
print(f"is n2 less than or equal to n3? {compare4}")

print('\n-----Example 10: String Indexing -----')
username = "peterpan123"
print(f"username = {username}")
print(f"The fifth character = {username[4]}")

# Positive indexing


# Negative indexing
print(f"The fifth last character =                       {username[-5]}")

print('\n-----Example 11: String slice -----')
# Slice from the beginning to the 4th character
print(f"Slice from the beginning to the 4th character = {username[:4]}")
# Slice from the 5th character to the end
print(f"Slice from the 5th character to the end =       {username[4:]}")
# Slice from the 3th to the 8th character
print(f"Slice from the 3th to the 8th character =       {username[2:8]}")

# Slice from the 4th to the 6th character using negative indexing
print(f"Slice from the 3th to the 8th character with step of 2 = {username[-8:-5]}")

print('\n-----Example 12: total  characters in a string (len) -----')
print(f"The username has = {len(username)} characters")

print('\n-----Example 13: strip()  method-----')
username = "          peterPAN123          "
print(f"The username =                         {username}. End of username")
username = username.strip()
print(f"The username after method strip =      {username}. End of username")

print('\n-----Example 14: upper and lower()  method-----')
username = username.lower()
print(f"The username after method lower =      {username}. End of username")
print(f"The username after method upper =      {username}. End of username")

print('\n-----Example 15: replace()  method-----')
username = username.replace('p', '%')
print(f"The username after replace method =      {username}. End of username")

print('\n-----Example 16: sprit()  method-----')
msg = "Introduction to Python Programming ! Today  we are learning split methods"
print(f"Message =                             {msg}")
print(f"Message  after split method =         {msg.split('!')}")

print('\n-----Example 17: find()  method-----')
# Find the letter 'P'
index_P = msg.find('P')
print(f"Index of letter P is =            {index_P}")
#  Find the second letter 'P'
sec_index_P = msg.find('P', index_P + 1)
print(f"Next index of letter P is =       {sec_index_P}")
# Find a non-existing letter 'Y'
index_Y = msg.find('Y')
print(f"The index of letter Y is =        {index_Y}") # -1 means  none.

print('\n-----Example 18: in, not in statement -----')
# Check if the word 'we' is in the  mgs string
answer_we = "we" in msg
print(f"is the word 'we' in the 'mgs' string?  =       {answer_we}")
answer_today = "Today" not in msg 
print(f"is the word 'Today' in the 'msg' string? =     {answer_today}")

print('\n-----Example 19: List Indexing -----')
colors = ["organge", "magenta", "olive", "Magenta"]
numbers = [6, 20, -9, 5, -12]
mixedlist = [False, 20, "Peter", True, -9, "peter"]
emptylist = []

print(f"colors list =                {colors}")
print(f"numbers list =               {numbers}")
print(f"empty list =                 {emptylist}")
print(f"Mixed list =                 {mixedlist}")

print(f"2nd colors =                 {colors[1]}")
print(f"1st numbers =                {numbers[0]}")
# print(f"3rd value =                  {emptylist[2]}") # can't return empty character

print(f"last colors list =           {colors[-1]}")
print(f"3rd last numbers =           {numbers[-3]}")

print('\n-----Example 20: +* operator on list -----')
# Concatenate the first with the last color
new_color = colors[0] + colors[-1]
print(f"The new color is =            {new_color}")
# C on catenate the 2nd color with the 3rd number
# new_word = colors[1] + numbers[2]  #--> data type error
# print(f"The new word is                  {new_word}")

print('\n-----Example 21: remove items from a list -----')
# Remove the 2nd last color
colors.pop(-1)
print(f"colors after pop =      {colors}")

print('\n-----Example 22: adding items to the list -----')
# Add  itesm to the end of list colors
colors.append("PINK")
print(f"color after append =          {colors}")
# Add a n ew list to a list
colors.append(["blue", "green"])
print(f"colors after append =         {colors}")
# Add multiple items to a list
# colors.append("RED", "PURPLE") # ----
# print(f"colors after append =         {colors}")

print('\n-----Example 23: sort method -----')
colors = ["organge", "magenta", "olive", "Magenta"]
print(f"color list =                 {colors}")
colors.sort()
print(f"color list sorted =          {colors}")

bool_list = [True, True, False]
bool_list.sort()
print(f"bool list sorted = {bool_list}")

print('\n-----Example 24: count method -----')
count_true = bool_list.count(True)
print(f"There is {count_true} True values")
count_red = colors.count("red")
print(f"There  is /are {count_red} red colors")

print('\n-----Example 25: lenght of method -----')
lenght_colors = len(colors)
print(f"There is/are {lenght_colors} colors")

print('\n-----Example 26: index of a item in a list -----')
# index of color 'olive'
index_olive = colors.index("olive")
print(f"The index of color olive  is         {index_olive}")
# index of color 'green'
# index_green = colors.index('green') # ---> value error, can't return index of unexisting value
# print(f"The index of color green is          {index_green}")





