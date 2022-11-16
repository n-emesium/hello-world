import random

def game():
    file = ["rock", "scissors", "paper"]
    game_score = 0
    game_limit = 4
    game_over = False
    wins = 0
    losses = 0
    draws = 0
    while not game_over:
        game_score += 1
        if game_score == game_limit:
            game_over = True
        else:
            user_input = input("Please choose rock, paper, or scissors. ").lower()
            user_index = file.index(user_input)
            bot_choice = random.choice(file)
            bot_index = file.index(bot_choice)
            print("The bot chose: " + bot_choice)
            if (user_index + 1) % len(file) == bot_index:
                print("You win. ")
                wins += 1
                continue
            elif user_index == bot_index:
                print("It's a draw. ")
                draws += 1
                continue
            else:
                print("You lose. ")
                losses += 1
        
    print("Game over. ")
    print("Your wins are: " + str(wins))
    print("Your losses are: " + str(losses))
    print("Your draws are: " + str(draws))

    user_replay = input("Do you wish to replay? Yes or No? Please type in 'y' or 'n' for the corresponding answer. ").lower()
    if user_replay == "y":
        game_score = 0
        game_over = False
        wins = 0
        losses = 0
        draws = 0
        print("Starting anew! ")
        game()
    else:
        print("Alright then, good game. ")
    
game() 
    