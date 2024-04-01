def promptSkipDay():
    print('> Skipping the day. Goodnight..')
    
def promptEarlyCompleted(username):
    print(f"> Good job {username}! You completed early game phase!")
    
def promptCurrentDay(current_day, username,elixir):
    print(f'\n> [Day {current_day}] Good morning {username}, you can use {elixir} elixir points today!')
    
def remainingElixir(elixir_point):
    print(f'> Elixir points remaining: {elixir_point}')