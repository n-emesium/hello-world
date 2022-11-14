from random import *

guard_count = 0
bullet_count = 0
bot_guard_count = 0
bot_bullet_count = 0
game_over = False
opts = ["guard", "bullet"]
user_decision = opts
bot_decision = opts

while not game_over:
    user_choice = input("Guard or bullet? ").lower()
    if user_choice == opts[0]:
        guard_count += 1
        print("Your guard count is: ", guard_count)
    elif user_choice == opts[1]:
        bullet_count += 1
        print("Your bullet count is: ", bullet_count)
    bot_choice = choice(opts)
    if bot_choice == opts[0]:
        bot_guard_count += 1
        print("The bot's guard count is: ", bot_guard_count)
    elif bot_choice == opts[1]:
        bot_bullet_count += 1
        print("The bot's bullet count is: ", bot_bullet_count)
    print("Start game. ")
    user_decision = input("Guard or use bullet? ").lower()
    if user_decision == opts[0]:
        if guard_count > 0:
            guard_count -= 1
            print("Your guard count is: ", guard_count)
        else:
            print("You don't have any guards left. ")
            if bullet_count > 0:
                user_decision = opts[1]
                print("You will shoot the bot. ")
                bot_guard_count -= 1
            else:
                print("You don't have enough bullets. ")
                bot_guard_count = bot_guard_count
    elif user_decision == opts[1]:
        bullet_count -= 1
        bot_guard_count -= 1
        print("Your bullet count is:", bullet_count)
    bot_decision = choice(opts)
    if bot_decision == opts[0]:
        if bot_guard_count > 0:
            bot_guard_count -= 1
            print("The bot chose to guard, and the bot's guard count is: ", bot_guard_count)
        else:
            bot_decision = opts[1]
            print("The bot is out of guards, it will shoot. ")
            if bot_bullet_count == 0:
                guard_count = guard_count
                print("It doesn't have enough bullets. ")
            else:
                guard_count -= 1
    elif bot_decision == opts[1]:
        if bot_bullet_count > 0:
            bot_bullet_count -= 1
            if user_decision == opts[0]:
                guard_count = guard_count
            else:
                guard_count -= 1
            print("The bot chose to shoot, and the bot's bullet count is:", bot_bullet_count)
        else:
            bot_decision = opts[0]
            print("The bot is out of bullets, it will guard. ")
            if bot_guard_count == 0:
                print("It has no guards left, you win. ")
                continue
            else:
                bot_guard_count -= 1
    print("Let's look at the results. The bot's guard count is: ", bot_guard_count, "And your guard count is: ", guard_count)
    if bot_guard_count == 0 and guard_count == 0:
        print("The scores will now reset. ")
        continue
    elif bot_guard_count < 0 and guard_count >= 0:
        print("You lose. ")
        game_over = True
    elif guard_count < 0 and bot_guard_count >= 0:
        print("You win. ")
        restart_or_no = input("Do you wanna restart or no? ")
        break
    elif bot_guard_count == guard_count:
        print("No one wins, you both pass for this round. ")
    elif user_decision == opts[1] and guard_count == 0 and bot_decision == opts[1] and bot_guard_count == 0:
        print("It's a tie. ")
        continue