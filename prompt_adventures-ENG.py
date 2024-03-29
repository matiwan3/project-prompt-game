#!/usr/bin/env python3
# MIRO BOARD: https://miro.com/app/board/uXjVKavmm8k=/?share_link_id=408092236856
from inGameQuests.quests_quizzes import mathExercise_1
from inGameActions.actions_setup import unitSelect, setCharacterName
from textPrompts.system_prompts import everythingIsSetUp, startingGame, welcomePrompt
        
def main():
    # Game settings
    run = True
    earlyGameDays = 5
    midGameDays = 14
    lateGameDays = 32
    sounds = True
    
    while run: 
        welcomePrompt()
        username = setCharacterName()
        unit = unitSelect(username)
        if unit == 0:
            break
        everythingIsSetUp()
        mainGame = True
        while mainGame:
            for x in range(earlyGameDays):
                print('Early game day ',(x + 1))
                
            for y in range(midGameDays):
                print('Mid game day ',(y + 1))
                
            for z in range(lateGameDays):
                print('Late game day ',(z + 1))
                
            mainGame = False
        
        # quiz_result = mathExercise_1()
        # unit.intelligence += quiz_result
        # print(f'Your current intelligence is {unit.intelligence}')
        run = False
    
if __name__ == '__main__':
    startingGame()
    main()