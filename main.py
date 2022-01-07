import tkinter as tk

from numpy import number
from bot import *

def RunBot():
    numberOfBrowsers = numberOfBrowsersInput.get()
    timeToWaitForPageToLoad = timeToWaitForPageToLoadInput.get()
    timeBetweenActions = timeBetweenActionsInput.get()
    restDuration = restDurationInput.get()
    workDuration = workDurationInput.get()
    print("Number of browsers: " + numberOfBrowsers)
    print("time to wait for page to load: " + timeToWaitForPageToLoad)
    print("time between actions: " + timeBetweenActions)
    print("Rest Duration: " + restDuration)
    print("Work Duration: " + workDuration)
    root.destroy()
    runProgram(numberOfBrowsers, timeToWaitForPageToLoad, timeBetweenActions, restDuration, workDuration)

root = tk.Tk()
root.grid_columnconfigure((0,1), weight=1)
root.geometry("600x200")
root.title("Bomb Crypto Bot") 

numberOfBrowsersLabel = tk.Label(root, text="number of browsers")
timeToWaitForPageToLoadLabel = tk.Label(root, text="time to wait for page to load")
timeBetweenActionsLabel = tk.Label(root, text="time between actions")
restDurationLabel = tk.Label(root, text="rest duration")
workDurationLabel = tk.Label(root, text="work duration")

numberOfBrowsersInput = tk.Entry(root)
timeToWaitForPageToLoadInput = tk.Entry(root)
timeBetweenActionsInput = tk.Entry(root)
restDurationInput = tk.Entry(root)
workDurationInput = tk.Entry(root)


# set default values
numberOfBrowsersInput.insert(0, numberOfBrowsers)
timeToWaitForPageToLoadInput.insert(0, timeToWaitForPageToLoad)
timeBetweenActionsInput.insert(0, timeBetweenActions)
restDurationInput.insert(0, restDuration)
workDurationInput.insert(0, workDuration)

# create button
runBotButton = tk.Button(text='Run Bot', command=lambda : RunBot())

numberOfBrowsersLabel.grid(row=1, column=0)
numberOfBrowsersInput.grid(row=1, column=1, sticky="ew")
timeToWaitForPageToLoadLabel.grid(row=2, column=0)
timeToWaitForPageToLoadInput.grid(row=2, column=1, sticky="ew")
timeBetweenActionsLabel.grid(row=3, column=0)
timeBetweenActionsInput.grid(row=3, column=1, sticky="ew")
restDurationLabel.grid(row=4, column=0)
restDurationInput.grid(row=4, column=1, sticky="ew")
workDurationLabel.grid(row=5, column=0)
workDurationInput.grid(row=5, column=1, sticky="ew")
runBotButton.grid(row=7, columnspan=2, sticky="ew", pady=10)

root.mainloop()