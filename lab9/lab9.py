"""
Sally Han
April 24, conditional statement
"""
print("\n-----exampe 1 and 2: if statement -----")    # no f, no variable
age = 20
agecode = 123

if age >= 21: # Check this is true, then execute next line
    print("You are an adult!") # False, not run next line
    agecode = 200
else: # Else has no condition, because 'anything else', 'anyother all'  means no need condition
    print("You are  under 21")  # Automatic indented for next line
    agecode = 100

print(f"\After the 'if' statement, agecode = {agecode}")

print("\n-----example 3: multi statement -----")
age = 20
if 0 <=  age <21: 
    print("You are minor!")
elif 21 <= age < 65:
    print("You are an adult!")
elif 65 <= age <= 130:
    print("You are  a senior citizen!")
else:
    print("Unable to read age! ")

print("\n-----example 4: and operator -----")
temperature = 80
humidity = 100

if 70 <= temperature <= 90 and humidity < 80 :
    print("The weather is pleasant")
else :
    print("The weather is not ideal")

print("\n-----example 5: or operator -----") 
day = "Sunday"
is_holiday = False

if day == "Saturday" or "Sunday" or is_holiday :
    print("You can relax today")
else: 
    print("It is a workday")

print("\n-----example 6: nested conditional statement -----") 
number = int(input("Enter a number: "))
if (number >= 0) :
    if number == 0:
        print("The number is zero")
    else:
        print(f"{number} is positive")
else: 
    print(f"{number} is negative")

print("\n-----example 7: username validation -----")
# User ame validation. uersename must have 3+ characters.
username = input("Enter a username: ")
username = username.strip()
len_username = len(username)
if  len_username >= 3:
     print(f"{username} has 3+ characters.")
     index_whitespace = username.find(" ")
     if index_whitespace == -1:
         print(f"{username} is valid")
     else:
         print(f"Username CANNOT have whitespace")
else:
    print(f"{username} is INVALID. Username must have 3+ character")

print("\n-----example 8 : match-case statement -----")
response_code = 404

match response_code:
    case  400:
        print(f"Code  = {response_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code = {response_code}. Server refused to send back")
    case 404: 
        print(f"Code = {response_code}. Server  can't  find")
    case _: #_: is anythning else.
        print("INVALID CODE")
