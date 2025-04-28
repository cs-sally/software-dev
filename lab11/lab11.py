"""
Sally Han
April 27, Pythnon applications
"""

#  import 'math' module
import math 
# import all from file "lab11_functions" 
from lab11_functions import *

print("\n----- Example 1: Python dictionary ----- ")
# create a dictionary
car = {
    "brand": "Ford", # key : value
    "model": "Mustang",
    "year": 1964
}
# print a complete dictionary
print(car)

# to access items in a dictionary we use [],  where [] goes the key's name
print(f"The year of the car is =  {car["year"]}")
# update the value of the key
car["year"] =1980
print(f"The year of the car was updated to = {car['year']}")
print("The year of the car was updated to = ", car['year'])
# add key:value pair
car["color"] = "red"
print(car)

print("\n Loop through each key in the dictionary")
for k in car:
    print(k)
print("\n Loop through each value in the dictionary")
for k in car:
    print(car[k])
print("\n Loop through each pair in the dictionary")
for k in car:
    print(f"{k} has value = {car[k]}")

print("\n----- Example 2: Python dictionary application ----- ")
# given the following list, create a  dictionary that will counts the number of times that a word appears in the string.
# create a dictionary  will organize the words as the keys, and the number of occurency of the word as the value of the key
phrase = "to be or not to be"
print(f"original phrase = {phrase}")
phrase_split = phrase.split()
print(f"splitted phrase = {phrase_split}")
# create the dictionary
word_count_dict = {}
# loop to each word in the list
for word in phrase_split:
    print(word)
    if word in word_count_dict:
        word_count_dict[word] +=1
    else: 
        word_count_dict[word] =1
# print result
print("Result of dictionary: ")
for w in word_count_dict:
    print(f"'{w}'= {word_count_dict[w]}")

print("\n----- eample 3: function that doesn't return values ----- ")
# call function 'greeting'
greeting()

print("\n----- example 4: function with parameter -----")
#  call function 'printusername'
printusername("Peter, Pan")
printusername("Prof. Wu")

print("\n---example 5, function with default paramenters")
user_country("Martha", "Chile")
user_country("Anna")
user_country("","France")

print("\n---example 6, function with return value")
num1 = 2
num2 = 5
prod1  = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")
prod1 = product(num1)
print(f"The product is = {prod1}")
prod1 = product()
print(f"The product is = {prod1}")

print("\n---example 7: Boolean function----")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} multiple of 3? {checknum2}")

print("\n---example 8: composition function----")
# test collectnum()
#number = collectnum(10)
#print(number)
# test sumnembers()
sumall = sumnumbers(3)
printresult(sumall)

print("\n---example 9: built-in function----")
r = 2
a  =  areaprint(r)
areaprint(a,r)

print("\n ex10")
ratio = ratio_hour(5)
print(ratio)
try:
    ratio = ratio_hour
except:
    print("Error with the function")
print(ratio)
