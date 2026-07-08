print("=" * 50)
print("Welcome to the Interactive personal Data collector!")
print("=" * 50)

print("\n This program collects your personal information.")
print("Please enter the required details.\n")

#Taking user input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
fav_number = int(input("Enter your favorite number: "))
print("\n")
print("=" * 50)
print("collected information")
print("=" * 50)

print(f"Name: {name}")
print(f"type: {type(name)}")
print(f"memory address: {id(name)}")

print()

print(f"Age: {age}")
print(f"type: {type(age)}")
print(f"memory address: {id(age)}")

print()

print(f"Height: {height}")
print(f"type: {type(height)}")
print(f"memory address: {id(height)}")

print()

print(f"Favorite Number: {fav_number}")
print(f"type: {type(fav_number)}")
print(f"memory address: {id(fav_number)}")

print()

birth_year = 2026 - age

print(f"Your birth year is: {birth_year}")   

print()

height_int = int(height)

print(f"original height: {height}")
print(f"height after converting to int: {height_int}")

print()

print("Thank you for using the personal data collector!")
print("keep learning python. goodbye!")
