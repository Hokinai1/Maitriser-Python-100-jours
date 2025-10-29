# Stocker les nom dans une variable
name = "Vivian"
nameOfPerson = "Aranha"

# Stocker l'âge dans une variable
age = 42

# String
name = "Vivian"

# Integer
age = 42

# Float
height = 5.8

# Boolean
is_student = False

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

age = "42"

myAge = int(age)

print(myAge + 5)

name = "Vivian"

print("Hello, " + name + "!")

print("Hello My Friend, {}!".format(name))

print(f"Hello, {name}!")

# Personalized Greeting Program

# Step 1: Ask for user details
name = input("Quel est votre nom? ")
age = int(input("Quel age avez-vous? "))
color = input("Quelle est votre couleur favorite ? ")

# Step 2: Generate a personalized greeting message
print("\n---- Personnaliser la Salutation ----")
print(f"Salu, {name}! 👋")
print(f"Vous avez {age} ans et {color} est votre couleur préféreé!")
print("Vous êtes maintenant prêt a embrasser une nouvelle aventure en python 🚀🐍")