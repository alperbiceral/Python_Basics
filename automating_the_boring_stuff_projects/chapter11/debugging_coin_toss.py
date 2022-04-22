import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
# added part start
if guess == 'heads':
    guess_no = 1
else:
    guess_no = 0
# added part end

toss = random.randint(0, 1) # 0 is tails, 1 is heads
print(toss)
if toss == guess_no:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    # added part start
    if guess == 'heads':
        guess_no = 1
    else:
        guess_no = 0
    # added part end

    if toss == guess_no:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')