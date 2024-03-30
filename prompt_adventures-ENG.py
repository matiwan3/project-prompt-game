#!/usr/bin/env python3
# MIRO BOARD: https://miro.com/app/board/uXjVKavmm8k=/?share_link_id=408092236856
from inGameQuests.quests_quizzes import mathExercise_1
from inGameActions.actions_setup import unitSelect, setCharacterName
from textPrompts.prompts_system import promptSetUp, promptStartingGame, promptWelcome, promptQuitting
from textPrompts.prompts_adventure import promptSkipDay, promptEarlyCompleted, promptCurrentDay
        
def main():
    # Game settings
    run = True
    current_day = 0
    earlyGameDays = 5
    midGameDays = 14
    lateGameDays = 32
    
    
    promptWelcome()
    username = setCharacterName()
    
    while run: 
        unit = unitSelect(username)
        if unit == 0:
            break
        promptSetUp()
        earlyGame = True
        midGame = False
        lateGame = False
        while earlyGame:
            promptCurrentDay(current_day, username)
            menuAction = input('Select action: \n1. Arena \n2. Taverna\n3. Event\n4. Quit the game\n[Any other input will cause skipping the current day]\nYour choice: ')
            if menuAction == '1':
                print('arena()')
            elif menuAction == '2':
                print('tavern()')
            elif menuAction == '3':
                print('event()')
            elif menuAction == '4':
                promptQuitting()
                break
            else:
                promptSkipDay()
            
            current_day += 1
            if current_day == earlyGameDays:
                promptEarlyCompleted(username)
                earlyGame = False 
                
                
        # quiz_result = mathExercise_1()
        # unit.intelligence += quiz_result
        # print(f'Your current intelligence is {unit.intelligence}')
        run = False
    
if __name__ == '__main__':
    promptStartingGame()
    main()