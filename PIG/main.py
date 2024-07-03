import random

def roll():
    min_val = 1
    max_val = 5
    roll = random.randint(min_val, max_val)

    return roll

#set up the game 

while True:
    players = input("Enter the no. of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("must be between 2 to 4 players")
    else:
        print('invalid no. try again')

max_score =  20
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print('\nPlayer Number', player_idx + 1, "Turn has just started!")
        print("your total score is", player_scores[player_idx], "\n")
        current_score = 0
        
        while True:
            should_roll = input('would you like to roll(y)? ')
            if should_roll.lower() != 'y':
                break        

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("you roll a:", value)
            print("your score is:", current_score)

        player_scores[player_idx] += current_score
        print('your total score is :', player_scores[player_idx])


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player number", winning_idx + 1, "is the winner with a score of", max_score)


