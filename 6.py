import random
import matplotlib.pyplot as plt
import time

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

# Wager increases 2 folds if the previousWager is lost
def doubler_bettor(funds, initial_wager, wager_count):
    global broke_count
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            #print('Won the last wager')
            if rollDice():
                value += wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    #print("We went broke after", currentWager, 'bets')
                    broke_count += 1
                    break

        elif previousWager == 'loss':
            #print('Doubling now!!')

            if rollDice():
                wager = previousWagerAmount * 2
                #print('We won', wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)

            else:
                wager = previousWagerAmount * 2
                #print('We lost', wager)
                value -= wager
                if value < 0:
                    #print('We went broke after', currentWager, 'bets')
                    broke_count += 1
                    break
                #print(value)
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
        currentWager += 1
    #print(value)
    plt.plot(wX, vY)


def simple_bettor(funds, initial_wager, wager_count):
    global broke_count
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
        broke_count += 1

    plt.plot(wX, vY)

x = 0
broke_count = 0
while x < 1000:
    simple_bettor(10000, 100, 1000)
    x += 1

print('Death Rate: ', (broke_count / float(x)) * 100 )
print('Survival Rate: ', 100 - ((broke_count / float(x)) * 100))

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()

'''

xx = 0
broke_count = 0
while xx < 1000:
    doubler_bettor(10000, 100, 100)
    xx += 1

print('Death Rate: ', (broke_count / float(xx)) * 100 )
print('Survival Rate: ', 100 - ((broke_count / float(xx)) * 100))
plt.axhline(0, color = 'r')
plt.show()

'''
