import random
import pyautogui
import time

backbutton = 'imgs/backbutton.png'
treasurehunt = 'imgs/treasurehunt.png'
heroes = 'imgs/heroes.png'
workall = 'imgs/workall.png'
restall = 'imgs/restall.png'
heroesback = 'imgs/heroesback.png'

addRest = True
numberOfBrowsers = 5
timeToWaitForPageToLoad = 10
timeBetweenActions = 3
restDuration = 3000
workDuration = 1000

resting = True

def randomNumber(number):
    maxRange = number + 20
    minRange = number - 20
    return random.randint(minRange,maxRange)

def ClickImageForAll(img):
    #back to main menu
    timeWaited = 0
    locations = pyautogui.locateAllOnScreen(img, confidence = 0.9)
    locationCount = sum(1 for x in locations)
    
    while(locationCount < numberOfBrowsers and timeWaited < timeToWaitForPageToLoad):
        time.sleep(1)
        timeWaited+=1
        locations = pyautogui.locateAllOnScreen(img)
        locationCount = sum(1 for x in locations)    
        print('browser found:' + str(locationCount) + "/" + str(numberOfBrowsers) + '    searching for: ' + str(timeWaited))
    
    print('all locations found succeeded:' + str(locationCount))
    for i in pyautogui.locateAllOnScreen(img, confidence = 0.9):
        pyautogui.click(i)

    time.sleep(timeBetweenActions)

def WaitForNextCycle():
    timeWaited = 0
    timeInTreasureHunt = 0
    timeToWait = restDuration
    timeToWait = restDuration if resting else workDuration
    while(timeWaited < timeToWait):
        time.sleep(1)

        timeWaited+=1
        timeInTreasureHunt+=1
        if timeInTreasureHunt >= 200:
            ClickImageForAll(backbutton)
            ClickImageForAll(treasurehunt)
            timeInTreasureHunt = 0

        if(resting):
            
            print('resting time left: ' + str(timeToWait - timeWaited))
        else:
            print('working time left: ' + str(timeToWait - timeWaited))

    runProgram(numberOfBrowsers, timeToWaitForPageToLoad, timeBetweenActions, restDuration, workDuration)

def runProgram(nob, tfpl, tba, rd, wd):
    global numberOfBrowsers
    global timeToWaitForPageToLoad
    global timeBetweenActions
    global restDuration
    global workDuration
    global resting

    time.sleep(1)
    ClickImageForAll(backbutton)
    ClickImageForAll(heroes)

    if addRest:
        if(resting):
            ClickImageForAll(workall)
            restDuration = randomNumber(int(rd))
        else:
            ClickImageForAll(restall)
            workDuration = randomNumber(int(wd))
        resting = not resting

    ClickImageForAll(heroesback)
    ClickImageForAll(treasurehunt)

    numberOfBrowsers = int(nob)
    timeToWaitForPageToLoad = int(tfpl)
    timeBetweenActions = int(tba)

    WaitForNextCycle()


