import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROB = 10

def generate_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expr = str(left) + " " + operators + " " + str(right)
    ans = eval(expr)
    return expr, ans

wrong = 0
input("Press Enter to start!")
print("---------------------------------")

start_time = time.time()


for i in range(TOTAL_PROB):
    expr, ans = generate_problems()
    while True:
        guess = input("Problem # " + str(i+1) + " : " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("---------------------------------")
print("Excellent work!!!!!!!!! You finished in", total_time, "seconds!.")