lowPointValue = 1
mediumPointValue = 4
highPointValue = 7

def promptCongratulations():
    print('Congratulations! This is the right answer.')

def promptWrongAnswer():
    print("You didn't get it right...")

def promptQuestionValue(pointValue):
    print(f'Welcome to math exercise. After solving the question you will gain {pointValue} intelligence point.')

# math quiz
def mathExercise_1():
    promptQuestionValue(lowPointValue)
    user_guess = input(f'\nQuestion: 1 + 3 = ...\nYour guess: ')
    if user_guess == '4':
        promptCongratulations()
        return lowPointValue
    promptWrongAnswer()
    return 0