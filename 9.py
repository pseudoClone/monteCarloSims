import random
import matplotlib.pyplot as plt
import time


startingFunds = 10000
wagerSize = 100
wagerCount = 10000
sampleSize = 1000

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
def doubler_bettor(funds, initial_wager, wager_count,color):
    global doubler_busts
    global doubler_profits
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
                if value <= 0:
                    #print("We went broke after", currentWager, 'bets')
                    doubler_busts += 1
                    break

        elif previousWager == 'loss':
            #print('Doubling now!!')

            if rollDice():
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                #print('We won', wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)

            else:
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                #print('We lost', wager)
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print('We went broke after', currentWager, 'bets')
                    doubler_busts += 1
                    break
                #print(value)
        currentWager += 1
    #print(value)
    plt.plot(wX, vY, 'c') # Douubler_bettor is cyan
    if value > funds:
        doubler_profits += 1


def simple_bettor(funds, initial_wager, wager_count,color):
    global simple_busts
    global simple_profits
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
        simple_busts += 1

    plt.plot(wX, vY,'k') # Black
    if value > funds:
        simple_profits += 1

x = 0
simple_busts = 0.0
simple_profits = 0.0
doubler_busts = 0.0
doubler_profits = 0.0



while x < sampleSize:
    simple_bettor(startingFunds, wagerSize, wagerCount,'k')
    doubler_bettor(startingFunds, wagerSize, wagerCount,'c')
    x += 1

print ('Simple Bettor Bust Chances:', (simple_busts/sampleSize) * 100)
print ('Doubler Bettor Bust Chances:', (doubler_busts/sampleSize) * 100)

print ('Simple Bettor Profit Chances:', (simple_profits/sampleSize) * 100)
print('Doubler Bettor Profit Chances:', (doubler_profits/sampleSize) * 100)

plt.axhline(0,color = 'r')

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
