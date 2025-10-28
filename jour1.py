# Projet du premier jour : Générateur du message de bienvenue basé sur l'entréé des utilisateur
from datetime import date, time, datetime

## Creating a date object
current_date = date.today()


# ## Creating a time object (from current datetime)
# current_time = datetime.now().time()
# print(f"Current time: {current_time}")

## Creating a datetime object
current_datetime = datetime.now()
print(f"Current datetime: {current_datetime}")




nom = input ("Quel est votre nom ? :")
hobby = input("Quel est votre passe temps préféré ?  :")

# \n = ajoute une ligne
# \t = ajoute une nouvelle tabulation

print("\n--- Message de bienvenu---")
print(f"Bonjour, {nom}!👋 : {current_date}, {current_datetime}") 
print(f"C'est génial de savoir ce que vous aimez : {hobby}.")
print(f"Apprêtez-vous à contruire quelque chose de beau aujourd'hui!")
