print("Welcome to the quiz game")
playing = input("Do you want to paly? ")
if playing.lower() != "yes":
    quit()
print("Okay lets play :)")
score = 0 

answer = input("What is the best Programming Language? ")
if answer == "python":
    print("correct!")
    score+=1

else:
    print("Incorrect :( ")

answer = input("Who invented pyhton? ")
if answer == "Guido van Rossum":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("who uses python? ")
if answer == "MAANG companies":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("What is the Characteristics of Python? ")
if answer == "Versatile":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("What is python coding? ")
if answer == "interpreted & Object oriented":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("Which one is Easy Python or Java? ")
if answer == "python":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("Where Python is Used? ")
if answer == "Web Development, Data science, AI":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("Why do you use python? ")
if answer == "python is easier to code":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("What is the feature of python? ")
if answer == "Open source":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

answer = input("Advantage of python? ")
if answer == "python is fun to code":
    print("correct!")
    score+=1
else:
    print("Incorrect :( ")

print("You got " + str(score) + " questons correct!!!.....")
print("You got " + str((score/10)*100) + " %.....")

