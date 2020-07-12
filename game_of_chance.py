import random

money = 100

#Write my game of chance functions here

#coin flip
def flip_call(guess, bet):
    #bet must be above 0, and no greater than money owned
    if bet <= 0:
        print("-----------------")
        print("This isn't a free game")
        print("Please bet more money")
        print("-----------------")
        return 0
    elif bet > money:
        print("-----------------")
        print("You do not have enough money to make this bet")
        return 0

    #This is the randomization function
    print("-----------------")
    print("Let's flip the coin!! You bet on " + guess + "!")
    result = random.randint(1,2)

#Function determines win or loss and returns bet to flip call
    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails!")

    if (result == 1 and guess == "Heads") or (result == 2 and guess == "Tails"):
        print("You won!")
        return bet
    elif (result == 1 and guess == "Tails") or (result == 2 and guess == "Heads"):
        print("I'm sorry. Money please")
        return -bet

#Cho-han
def cho_han(guess, bet):
    #bet must be above 0, and no greater than money owned
    if bet <= 0:
        print("-----------------")
        print("This isn't a free game")
        print("Please bet more money")
        print("-----------------")
        return 0
    elif bet > money:
        print("-----------------")
        print("You do not have enough money to make this bet")
        return 0

    #naming the dice variables and adding them together
    print("-----------------")
    print("Rolling the dice! Pick even or odd")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    print("The total is " + str(result) + "!")

    #Function determines even or odd and returns bet
    if guess == "Even" and result % 2 == 0:
        print("You won!")
        return bet
    elif guess == "Odd" and result % 2 == 1:
        print("You won!")
        return bet
    else:
        print("I'm sorry, money please")
        return -bet

#Card Draw game
def card_draw(bet):
    #Parameters of bet
        #bet must be above 0, and no greater than money owned
        if bet <= 0:
            print("-----------------")
            print("This isn't a free game")
            print("Please bet more money")
            print("-----------------")
            return 0
        elif bet > money:
            print("-----------------")
            print("You do not have enough money to make this bet")
            return 0

#Playing the game
        print("-----------------")
        print("Draw a card")
        other_player_card = random.randint(1, 13)
        guess = random.randint(1, 13)

        if guess == 1:
            print("You drew a 2")
        elif guess == 2:
            print("You drew a 3")
        elif guess == 3:
            print("You drew a 4")
        elif guess == 4:
            print("You drew a 5")
        elif guess == 5:
            print("You drew a 6")
        elif guess == 6:
            print("You drew a 7")
        elif guess == 7:
            print("You drew an 8")
        elif guess == 8:
            print("You drew a 9")
        elif guess == 9:
            print("You drew a 10")
        elif guess == 10:
            print("You drew a Jack!")
        elif guess == 11:
            print("You drew a Queen!")
        elif guess == 12:
            print("You drew a King!")
        elif guess == 13:
            print("You drew an Ace!!")

        if other_player_card == 1:
            print("Your opponent drew a 2")
        elif other_player_card == 2:
            print("Your opponent drew a 3")
        elif other_player_card == 3:
            print("Your opponent drew a 4")
        elif other_player_card == 4:
            print("Your opponent drew a 5")
        elif other_player_card == 5:
            print("Your opponent drew a 6")
        elif other_player_card == 6:
            print("Your opponent drew a 7")
        elif other_player_card == 7:
            print("Your opponent drew an 8")
        elif other_player_card == 8:
            print("Your opponent drew a 9")
        elif other_player_card == 9:
            print("Your opponent drew a 10")
        elif other_player_card == 10:
            print("Your opponent drew a Jack!")
        elif other_player_card == 11:
            print("Your opponent drew a Queen!")
        elif other_player_card == 12:
            print("Your opponent drew a King!")
        elif other_player_card == 13:
            print("Your opponent drew an Ace!!")



        if guess > other_player_card:
            print("You won!")
            return bet
        elif guess < other_player_card:
            print("I'm sorry, please pay")
            return -bet
        else:
            print("It's a tie!")
            return 0


#Game of Roullette\
#I do not yet understand how to place multiple bets e.g. "Black, even, 23, 22"
def roullette(guess, bet):
#Parameters of bet
    #bet must be above 0, and no greater than money owned
        if bet <= 0:
            print("-----------------")
            print("This isn't a free game")
            print("Please bet more money")
            print("-----------------")
            return 0
        elif bet > money:
            print("-----------------")
            print("You do not have enough money to make this bet")
            return 0

#Rolling the ball
        result = random.randint(0, 37)
        print("-----------------")
        print("Let's play roullette!!")
        if guess == "Even":
            print("You placed your bet on even numbers")
        elif guess == "Odd":
            print("You placed your bet on odd numbers")
        elif guess == "00":
            print("You placed your bet on 00!")
        else:
            print("You placed your bet on " + str(guess))

        if result == 37:
            print("It hit 00!")
        else:
            print("It hit " + str(result) + "!")

#Determines win or loss
        if guess == result or (guess == "00" and result == 37):
            print("You won!")
            return bet * 35
        elif guess == "00" and result == 37:
            print("You won!")
            return bet * 35
        elif (guess == "Even" and result % 2 == 0 and result != 0) or (guess == "Odd" and result % 2 == 1 and result != 37):
            print("You won!")
            return bet
        else:
            print("I'm sorry, you did not win. Please pay")
            return -bet






#Call my game of chance functions here
#Calling flip toss
money += flip_call("Tails", 5)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
#Calling cho_han
money += cho_han("Odd", 10)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
#Calling card Draw
money += card_draw(10)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
money += card_draw(10)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
#Calling roullette
money += roullette("Even", 10)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
money += roullette("Odd", 10)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
money += roullette(13, 5)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
money += roullette("00", 5)
print("you have " + str(money) + " dollars remaining")
print("-----------------")
