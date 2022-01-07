from numpy import number
import pyautogui
import time

backbutton = 'imgs/backbutton.png'
treasurehunt = 'imgs/treasurehunt.png'
heroes = 'imgs/heroes.png'
workall = 'imgs/workall.png'
restall = 'imgs/restall.png'
heroesback = 'imgs/heroesback.png'

numberOfBrowsers = 5
timeToWaitForPageToLoad = 10
timeToNextCycleInSeconds = 60

def SearchForImages(img):
    timeWaited = 0
    locations = pyautogui.locateAllOnScreen(img)
    locationCount = sum(1 for x in locations)
    while(locationCount < numberOfBrowsers):
        time.sleep(1)
        timeWaited+=1
        if timeWaited >= timeToWaitForPageToLoad:
            locations = pyautogui.locateAllOnScreen(img)
            locationCount = sum(1 for x in locations)    
        print('browser failed:' + str(locationCount) + '    time to search again: ' + str(timeWaited))
    return locationCount

def ClickImageForAll(img):
    #back to main menu
    locationCount = SearchForImages(img)
    print('all locations found succeeded:' + str(locationCount))
    for i in pyautogui.locateAllOnScreen(img):
        pyautogui.click(i)

    time.sleep(1)

def WaitForNextCycle(timeWaited):
    if timeWaited >= timeToNextCycleInSeconds:
        runProgram()
    else:
        time.sleep(1)
        timeWaited = timeWaited + 1
        print('time to next cycle: ' + str(timeToNextCycleInSeconds - timeWaited))
        WaitForNextCycle(timeWaited)

def runProgram():
    ClickImageForAll(backbutton)
    ClickImageForAll(heroes)
    ClickImageForAll(workall)
    ClickImageForAll(heroesback)
    ClickImageForAll(treasurehunt)
    WaitForNextCycle(0)


#initial run
runProgram()


