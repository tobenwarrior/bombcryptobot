import pyautogui
import time

backbutton = 'imgs/backbutton.png'
treasurehunt = 'imgs/treasurehunt.png'
heroes = 'imgs/heroes.png'
workall = 'imgs/workall.png'
restall = 'imgs/restall.png'
heroesback = 'imgs/heroesback.png'

def clickImageForAll(img):
    #back to main menu
    limitSearch = 1000
    locations = pyautogui.locateAllOnScreen(img)
    locationCount = sum(1 for x in locations)
    print(locationCount)
    while(locationCount < 5 or limitSearch < 10):
        time.sleep(3)
        locations = pyautogui.locateAllOnScreen(img)
        locationCount = sum(1 for x in locations)
        limitSearch+=1
    
    for i in pyautogui.locateAllOnScreen(img):
        time.sleep(0.5)
        pyautogui.click(img)

clickImageForAll(backbutton)
clickImageForAll(heroes)
clickImageForAll(workall)
clickImageForAll(heroesback)
clickImageForAll(treasurehunt)

