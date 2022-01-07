import pyautogui
import time

backbutton = 'imgs/backbutton.png'
treasurehunt = 'imgs/treasurehunt.png'
heroes = 'imgs/heroes.png'
workall = 'imgs/workall.png'
restall = 'imgs/restall.png'
heroesback = 'imgs/heroesback.png'

numberOfBrowsers = 5
timeToWaitForBrowser = 10
timeToNextCycleInSeconds = 60

def clickImageForAll(img):
    #back to main menu
    limitSearch = 0
    locations = pyautogui.locateAllOnScreen(img)
    locationCount = sum(1 for x in locations)
    while(locationCount < numberOfBrowsers and limitSearch < timeToWaitForBrowser):
        time.sleep(1)
        locations = pyautogui.locateAllOnScreen(img)
        locationCount = sum(1 for x in locations)
        limitSearch+=1
        print('browser failed:' + str(locationCount) + '    times searched: ' + str(limitSearch))
    
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
    clickImageForAll(backbutton)
    clickImageForAll(heroes)
    clickImageForAll(workall)
    clickImageForAll(heroesback)
    clickImageForAll(treasurehunt)
    WaitForNextCycle(0)


#initial run
runProgram()


