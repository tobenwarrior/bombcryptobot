from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
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
signaturerequest = 'imgs/signaturerequest.png'

addRest = True
numberOfBrowsers = 6
timeToWaitForPageToLoad = 5
timeBetweenActions = 3
restDuration = 1000
workDuration = 2000

timeWaited = 0

resting = True

def RandomNumber(number):
    maxRange = number + 20
    minRange = number - 20
    return random.randint(minRange,maxRange)

def ClickLocations(locations):
    for i in locations:
        pyautogui.click(i)

def Disconnect():
    isOk = pyautogui.locateAllOnScreen(ok, confidence = 0.9)
    isConnectWallet = pyautogui.locateAllOnScreen(connectwallet, confidence = 0.9)
    isSignIn = pyautogui.locateAllOnScreen(signin, confidence = 0.9)
    isSignatureRequest = pyautogui.locateAllOnScreen(signaturerequest, confidence = 0.9)
    disconnectedBrowsers =  sum(1 for x in isConnectWallet) + sum(1 for x in isOk) + sum(1 for x in isSignIn) + sum(1 for x in isSignatureRequest)
    isDisconnected = False


    for i in pyautogui.locateAllOnScreen(ok, confidence = 0.9):
        pyautogui.click(i)
    for i in pyautogui.locateAllOnScreen(connectwallet, confidence = 0.9):
        pyautogui.click(i)
    for i in pyautogui.locateAllOnScreen(signin, confidence = 0.9):
        pyautogui.click(i)
    for i in pyautogui.locateAllOnScreen(signaturerequest, confidence = 0.9):
        pyautogui.click(i)


    if(disconnectedBrowsers > 0):
        time.sleep(3)
        global timeWaited
        timeWaited = 0
        print("browsers disconnected: " + str(disconnectedBrowsers))
        isDisconnected = True
    return isDisconnected


def ClickImageForAll(img):
    # back to main menu
    global timeWaited
    timeWaited = 0
    locations = pyautogui.locateAllOnScreen(img, confidence = 0.9)
    locationCount = sum(1 for x in locations)
    
    while(locationCount < numberOfBrowsers and timeWaited < timeToWaitForPageToLoad):
        time.sleep(1)
        # check if disconnect
        timeWaitedForDisconnectedBrowser = 0
        while(Disconnect() and timeWaitedForDisconnectedBrowser < 5):
            time.sleep(1)
            timeWaited = 0
            timeWaitedForDisconnectedBrowser + 1
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

    print("number of browsers: " + str(numberOfBrowsers))
    print("time to wait for page to load: " + str(timeToWaitForPageToLoad))
    print("time between actions: " + str(timeBetweenActions))
    print("rest Duration: " + str(restDuration))
    print("work Duration: " + str(workDuration))

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


