import random

def game():
    pkmn = ["charmander", "bulbasaur", "squirtle"]
    print(pkmn)
    user_input = input("Please choose a Pokemon. ").lower()
    bot_input = random.choice(pkmn)
    bot_index = bot_input.index(pkmn)
    print("Congrats! You have chosen: " + user_input)
    print("Your opponent has chosen: " + bot_input)

    charmander_moves = ["scrath", "growl", "ember", "smokescreen", "dragon rage"]
    bulbasaur_moves = ["tackle", "growl", "leech seed", "vine whip", "poison powder", "sleep powder", "take down"]
    squirtle_moves = ["tackle", "tail whip", "water gun", "withdraw", "bubble", "bite"]
    
    if user_input.index(pkmn) == 0:
        print(charmander_moves)
        user_move_c = input("Please choose a move for charmander. ").lower()
        print("You used: " + user_move_c)

        
        


