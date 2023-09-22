#string concatenation 
#to put strings together
#player = "boxer" //some string variable
#a few ways to concatenate
#print("Arun is a"+ player)
#print("Arun is a {}".format(player))
#print(f"Arun is a {player}")


adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("famous person: ")

madlib = f"computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are a {famous_person}!."

print(madlib)
