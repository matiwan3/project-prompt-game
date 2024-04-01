#!/usr/bin/env python3
# MIRO BOARD: https://miro.com/app/board/uXjVKavmm8k=/?share_link_id=408092236856
from inGameQuests.quests_quizzes import mathExercise_1
from inGameActions.actions_setup import unitSelect, setCharacterName
from textPrompts.prompts_system import promptSetUp, promptStartingGame, promptWelcome, promptQuitting
from textPrompts.prompts_adventure import promptSkipDay, promptEarlyCompleted, promptCurrentDay, remainingElixir
from inGameQuests.quests_arena import arena
from inGameQuests.quests_tavern import tavern
        
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
            elixir_point = 2
            promptCurrentDay(current_day, username, elixir_point)
            while (elixir_point > 0):
                menuAction = input('\n> Select action: \n1. Arena ( -1 elixir)\n2. Tavern ( -1 elixir)\n3. Event ( -2 elixir)\n4. Quit the game\n> NOTE: Any other input will skip the current day\n> Your choice: ')
                if menuAction == '1':
                    elixir_point -= 1
                    remainingElixir(elixir_point)
                    arena()
                elif menuAction == '2':
                    elixir_point -= 1
                    remainingElixir(elixir_point)
                    tavern()
                elif menuAction == '3':
                    elixir_point -= 2
                    remainingElixir(elixir_point)
                    print('> TODO: event()\n')
                elif menuAction == '4':
                    promptQuitting()
                    quit()
                else:
                    elixir_point = 0
                    promptSkipDay()
                
            current_day += 1
            if current_day == earlyGameDays:
                promptEarlyCompleted(username)
                earlyGame = False

        # quiz_result = mathExercise_1()
        # unit.intelligence += quiz_result
        # print(f'Your current intelligence is {unit.intelligence}')
if __name__ == '__main__':
    promptStartingGame()
    main()