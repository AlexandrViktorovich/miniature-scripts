import pyautogui
import keyboard

start = input('Start key:')
stop = input('Stop key:')

#You need to chose key for activation script
#Script work when u press on start key
#if u press stop key, script was close

while True:
    if keyboard.is_pressed(start):
        pyautogui.tripleClick()
    if keyboard.is_pressed(stop):
        break


