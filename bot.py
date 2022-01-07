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
timeToNextCycleInSeconds = 600

resting = True

def randomNumber(number):
    maxRange = number + 20
    minRange = number - 20
    return random.randint(minRange,maxRange)

def ClickImageForAll(img):
    #back to main menu
    timeWaited = 0
    locations = pyautogui.locateAllOnScreen(img)
    locationCount = sum(1 for x in locations)
    
    while(locationCount < numberOfBrowsers and timeWaited < timeToWaitForPageToLoad):
        time.sleep(1)
        timeWaited+=1
        locations = pyautogui.locateAllOnScreen(img)
        locationCount = sum(1 for x in locations)    
        print('browser found:' + str(locationCount) + "/" + str(numberOfBrowsers) + '    searching for: ' + str(timeWaited))
    
    print('all locations found succeeded:' + str(locationCount))
    for i in pyautogui.locateAllOnScreen(img):
        pyautogui.click(i)

    time.sleep(5)

def WaitForNextCycle(timeWaited):
    timeToWait = timeToNextCycleInSeconds
    while(timeWaited < timeToNextCycleInSeconds):
        time.sleep(1)
        timeWaited+=1
        print('time to next cycle: ' + str(timeToWait - timeWaited))
    runProgram()

def runProgram():
    ClickImageForAll(backbutton)
    ClickImageForAll(heroes)

    global resting
    if addRest:
        if(resting):
            ClickImageForAll(workall)
        else:
            ClickImageForAll(restall)
        resting = not resting

    ClickImageForAll(heroesback)
    ClickImageForAll(treasurehunt)

    global timeToNextCycleInSeconds
    timeToNextCycleInSeconds = randomNumber(timeToNextCycleInSeconds)
    WaitForNextCycle(0)


#initial run
runProgram()


