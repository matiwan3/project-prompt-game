from units.unit_archer import UnitArcher
from units.unit_guardian import UnitGuardian
from units.unit_mag import UnitMag
from units.unit_ninja import UnitNinja
from units.unit_warrior import UnitWarrior

unitClassNameArcher = 'Archer'
unitClassNameMag = 'Mag'
unitClassNameWarrior = 'Warrior'
unitClassNameNinja = 'Ninja'
unitClassNameGuardian = 'Guardian'

def unitSelect(username):
    chooseClass = input(f"Welcome {username}! It's time to select your unit class: \n1. {unitClassNameArcher}\n2. {unitClassNameMag}\n3. {unitClassNameWarrior}\n4. {unitClassNameNinja}\n5. {unitClassNameGuardian}\nYour choice: ")
    if chooseClass == '1':
        unit = UnitArcher()
    elif chooseClass == '2':
        unit = UnitMag()
    elif chooseClass == '3':
        unit = UnitWarrior()
    elif chooseClass == '4':
        unit = UnitNinja()
    elif chooseClass == '5':
        unit = UnitGuardian()
    else:
        print('[SYSTEM] Invalid choice!')
        return 0
    return unit

def setCharacterName():
    characterName = input('Choose your name: ')
    return characterName
