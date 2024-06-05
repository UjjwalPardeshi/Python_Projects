import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('write a number larger than 0')    
        quit
else:
    print('please type a number')
    quit()
         
random_number = random.randint(0, top_of_range) #1 -10

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time')
        continue

    if user_guess == random_number:
        print("you got it correct")
        break
    elif  user_guess > random_number:
            print('you were above the number!')
    else:
            print('you were below the number!')

print("you got it in ", guesses, "guesses")

# if top_of_range != random_number:
#     print('loser')