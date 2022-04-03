# this program provides 3 randomly created multiplication questions to the user 
import pyinputplus as pyip
import random

# count the number of correct answers to display the score
answer_counter = 0

# inform user about the rules
print("You have 3 rights and 8 seconds to answer")

# play 3 rounds
for i in range(3):
    # assign operands randomly
    operand1 = random.randint(0, 9)
    operand2 = random.randint(0, 9)
    answer = operand1 * operand2
    result = pyip.inputNum(prompt=f"{operand1} X {operand2} = ", limit=3, timeout=8, default=-1)

    # check the result
    if result == answer:
        answer_counter += 1
        print("Correct")
    else:
        print("Cannot find the correct answer")

# display the score
print(f"Number of correct answers is: {answer_counter}")