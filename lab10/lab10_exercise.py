"""
Sally Han
April , 
Lab 10 Exercise
"""

# Lab 10 exercise
print("\n-----Lab exercise-----")
colors = ['red', 'orange', 'olive', 'magenta', 'green']
color_input = input("Enter a color: ")
stripped_color = color_input.strip()
stripped_lowercase_color = stripped_color.lower()

found = False # Initializing Flag: "haven't found yet"

for existing_color in colors:
    if  stripped_lowercase_color == existing_color:
        print(f"The {stripped_lowercase_color} is in the list")
        found = True
        break # Exit the loop once found
if not found:
    print(f"The {stripped_lowercase_color} IS NOT in the list")

