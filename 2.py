import random

def rollDice():
    roll = random.randint(1,100)
    if(roll == 100):
        #print(roll, 'Play again')
        return False
    elif (roll <= 50):
        #print(roll,'Play again')
        return False
    elif (roll < 100 and roll > 50):
        #print(roll, 'You win!')
        return True


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    currentWager = 0

    while(currentWager < wager_count):
        if rollDice():
            value += wager
        else:
            value -= wager
        currentWager += 1

    if value < 0:
        print('Broke,', 'Funds:',value)
    else: 
        print('Rich,', 'Funds:',value)
x = 0
while(x < 100):
    simple_bettor(10000, 100, 10000)
    x += 1
