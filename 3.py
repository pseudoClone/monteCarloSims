import random
import matplotlib.pyplot as plt

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

    wX = []
    vY = []

    currentWager = 1

    while(currentWager <= wager_count):
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    if value < 0:
        print('Broke,', 'Funds:',value)
    else: 
        print('Rich,', 'Funds:',value)

    plt.plot(wX, vY)
x = 0
while(x < 1000):
    simple_bettor(10000, 100, 1000)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')

plt.show()
