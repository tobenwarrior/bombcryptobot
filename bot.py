import random
import pyautogui
import time

backbutton = 'imgs/backbutton.png'
treasurehunt = 'imgs/treasurehunt.png'
heroes = 'imgs/heroes.png'
workall = 'imgs/workall.png'
restall = 'imgs/restall.png'
heroesback = 'imgs/heroesback.png'
ok = 'imgs/ok.png'
connectwallet = 'imgs/connectwallet.png'
signin = 'imgs/signin.png'
menulogo = 'imgs/menulogo.png'

addRest = True
numberOfBrowsers = 6
timeToWaitForPageToLoad = 10
timeBetweenActions = 3
restDuration = 1000
workDuration = 2000

resting = True

def RandomNumber(number):
    maxRange = number + 20
    minRange = number - 20
    return random.randint(minRange,maxRange)

def ClickLocations(locations):
    for i in locations:
        pyautogui.click(i)

def Disconnect():
    isInMenu = pyautogui.locateAllOnScreen(menulogo, confidence = 1)
    isOk = pyautogui.locateAllOnScreen(ok, confidence = 0.9)
    disconnectedBrowsers =  sum(1 for x in isInMenu) + sum(1 for x in isOk)
    isDisconnected = False

    for i in pyautogui.locateAllOnScreen(ok, confidence = 0.9):
        pyautogui.click(i)
    for i in pyautogui.locateAllOnScreen(connectwallet, confidence = 0.9):
        pyautogui.click(i)
    for i in pyautogui.locateAllOnScreen(signin, confidence = 0.9):
        pyautogui.click(i)

    if(disconnectedBrowsers > 0):
        print("browsers disconnected: " + str(disconnectedBrowsers))
        isDisconnected = True
    time.sleep(3)
    return isDisconnected


def ClickImageForAll(img):
    # back to main menu
    timeWaited = 0
    locations = pyautogui.locateAllOnScreen(img, confidence = 0.9)
    locationCount = sum(1 for x in locations)
    
    while(locationCount < numberOfBrowsers and timeWaited < timeToWaitForPageToLoad):
        time.sleep(1)
        # check if disconnect
        while(Disconnect()):
            time.sleep(0.5)
            timeWaited = 0
        timeWaited+=1
        locations = pyautogui.locateAllOnScreen(img)
        locationCount = sum(1 for x in locations)    
        print('browser found:' + str(locationCount) + "/" + str(numberOfBrowsers) + '    searching for: ' + str(timeWaited))
    
    print('all locations found succeeded:' + str(locationCount))
    for i in pyautogui.locateAllOnScreen(img):
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

    numberOfBrowsers = int(nob)
    timeToWaitForPageToLoad = int(tfpl)
    timeBetweenActions = int(tba)

    print("Number of browsers: " + str(numberOfBrowsers))
    print("time to wait for page to load: " + str(timeToWaitForPageToLoad))
    print("time between actions: " + str(timeBetweenActions))
    print("Rest Duration: " + str(restDuration))
    print("Work Duration: " + str(workDuration))

    time.sleep(1)
    ClickImageForAll(backbutton)
    ClickImageForAll(heroes)

    if addRest:
        if(resting):
            ClickImageForAll(workall)
            restDuration = RandomNumber(int(rd))
        else:
            ClickImageForAll(restall)
            workDuration = RandomNumber(int(wd))
        resting = not resting

    ClickImageForAll(heroesback)
    ClickImageForAll(treasurehunt)
    WaitForNextCycle()


