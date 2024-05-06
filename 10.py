import random
import matplotlib.pyplot as plt
import time


startingFunds = 10000
wagerSize = 100
wagerCount = 10000
sampleSize = 1000

lower_busts = 31.235
higher_profitss = 63.208

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



def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'

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
                    multiple_busts += 1
                    break

        elif previousWager == 'loss':
            #print('Doubling now!!')

            if rollDice():
                wager = previousWagerAmount * random_multiple
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
                wager = previousWagerAmount * random_multiple
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
                    multiple_busts += 1
                    break
                #print(value)
        currentWager += 1
    #print(value)
    #plt.plot(wX, vY, 'c') # Douubler_bettor is cyan
    if value > funds:
        multiple_profits += 1





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



while True:
    multiple_busts = 0.0
    multiple_profits = 0.0

    multipleSampSize = 100000
    currentSample = 1

    random_multiple = random.uniform(0.1, 10.0)
    while currentSample <= multipleSampSize:
        multiple_bettor(startingFunds, wagerSize, wagerCount)
        currentSample += 1

    if ((multiple_busts/multipleSampSize) * 100.00 < lower_busts) and ((multiple_profits/multipleSampSize) * 100.00 > higher_profitss):
        print('##################################################################')
        print('Found the winner, the multple was:', random_multiple)
        print('Lower Busts to beat:', lower_busts)
        print('Higher profits to beat:', higher_profitss)
        print('Bust rates:', (multiple_busts/multipleSampSize) * 100.00)
        print('Profit rate:', (multiple_profits/multipleSampSize) * 100.00)
        print('##################################################################')

    '''
    else:
        print('##################################################################')
        print('Found the loser, the multple was:', random_multiple)
        print('Lower Busts to beat:', lower_busts)
        print('Higher profits to beat:', higher_profitss)
        print('Bust rates:', (multiple_busts/multipleSampSize) * 100.00)
        print('Profit rate:', (multiple_profits/multipleSampSize) * 100.00)
        print('##################################################################')
    '''
