lowPointValue = 1
mediumPointValue = 4
highPointValue = 7

def congratulationsPrompt():
    print('Congratulations! This is the right answer.')

def wrongAnswerPrompt():
    print("You didn't get it right...")

def questionValuePrompt(pointValue):
    print(f'Welcome to math exercise. After solving the question you will gain {pointValue} intelligence point.')

# math quiz
def mathExercise_1():
    questionValuePrompt(lowPointValue)
    user_guess = input(f'\nQuestion: 1 + 3 = ...\nYour guess: ')
    if user_guess == '4':
        congratulationsPrompt()
        return lowPointValue
    wrongAnswerPrompt()
    return 0