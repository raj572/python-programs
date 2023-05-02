import pyautogui
import time
time.sleep(3)
count=0
limit=int(input('Enter how many times you want to send same message: '))
while count<=limit:
    pyautogui.typewrite(input())
    pyautogui.press('enter')
    count+=1
    
   