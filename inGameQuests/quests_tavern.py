from random import randint
CUPS = 0

def printCupsTable():
    print('table with cups')

def calculateReward(cups):
    BASE_GOLD = 5
    reward = cups**2 * BASE_GOLD
    return reward
    
def tavern():
    CUPS = int(input('[T] > Welcome to tavern. Now you will play "fake-cups" game. The MORE cups you choose to play with the GREATER reward you will get. Only one cup contains a reward.\n[T] > Choose how many cups you want in the game: '))
    
    winning_cup = randint(1,CUPS)
    
    # Debug
    print(winning_cup)
    print(f'[T] > Winning chances: {win_chance}%')
    for x in range(CUPS):
        print(f'[CUP {x + 1}]', end=" ")
        
    guess_cup = int(input("\n[T] > Guess a cup: "))
    print(f'Cups: {CUPS}')
    win_chance = 1 / CUPS
    
    reward = calculateReward(CUPS)
    
    if guess_cup == winning_cup:
        print(f'[T] > Congratulations - cup number "{guess_cup}" wins. You get {reward} gold!')
        return guess_cup,reward
    else:
        print('[T] > Miss..')
        return 0
    