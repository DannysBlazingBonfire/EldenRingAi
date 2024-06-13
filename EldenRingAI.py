#RannAI
import secrets
from multiprocessing import Process
import time
import keyboard
import pyautogui
import pydirectinput
import sys
import win32api, win32con
import asyncio #use this thread library to listen to buttons to start / quit script

class RannAI:

    def __init__(self):
        self.stopFlag = False

    def setStopflag(self,bool):
        self.stopFlag = bool

    def test(self):
        print("runs")

    def click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    #clicks mouse using windows api   
    def clickPosition(self,x,y):
        win32api.SetCursorPos( (x,y) )
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    #have thread randomize number and choose moving (moves)
    #moves (check)
    def moveRight(self):
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')
        time.sleep(0.01)

    def moveLeft(self):
        pydirectinput.keyDown('a')
        time.sleep(1)
        pydirectinput.keyUp('a')
        time.sleep(0.01)

    def moveForw(self):
        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')
        time.sleep(0.01)

    def moveBackw(self):
        pydirectinput.keyDown('s')
        time.sleep(1)
        pydirectinput.keyUp('s')
        time.sleep(0.01)

    #Rolls(check)
    def rollBack(self):
        pydirectinput.keyDown('s')
        time.sleep(0.01)
        pydirectinput.keyDown('space')
        pydirectinput.keyUp('space')
        pydirectinput.keyUp('s')
        time.sleep(0.01)

    def rollForw(self):
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('space')
        pydirectinput.keyUp('space')
        pydirectinput.keyUp('w')
        time.sleep(0.01)

    def rollLeft(self):
        pydirectinput.keyDown('a')
        time.sleep(0.01)
        pydirectinput.keyDown('space')
        pydirectinput.keyUp('space')
        pydirectinput.keyUp('a')
        time.sleep(0.01)

    def rollRight(self):
        pydirectinput.keyDown('d')
        time.sleep(0.01)
        pydirectinput.keyDown('space')
        pydirectinput.keyUp('space')
        pydirectinput.keyUp('d')
        time.sleep(0.01)

    #attacks
    def lightAtt(self):
        self.click()

    def heavyAttack(self):
        pydirectinput.keyDown('shift')
        pydirectinput.mouseDown()
        time.sleep(1)
        pydirectinput.keyUp('shift')
        pydirectinput.mouseUp()

    def skillAttack(self):
        pydirectinput.keyDown('shift')
        time.sleep(0.01)
        pydirectinput.mouseDown(button='right')
        time.sleep(0.01)
        pydirectinput.keyUp('shift')
        pydirectinput.mouseUp(button='right')
        time.sleep(0.7)
        
    def jumpAttack(self):
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('space')
        time.sleep(0.8)
        pydirectinput.keyDown('f')
        time.sleep(0.01)
        pydirectinput.keyUp('f')
        pydirectinput.keyUp('space')
        self.lightAtt()
        pydirectinput.keyUp('w')
        time.sleep(0.7)

    def rollForwAttack(self):
        self.rollForw()
        self.lightAtt()
    
    def doubleLight(self):
        self.lightAtt()
        time.sleep(0.5)
        self.lightAtt()
        
    def tripleLight(self):
        self.lightAtt()
        time.sleep(0.5)
        self.lightAtt()
        time.sleep(0.5)
        self.lightAtt()
    
    #other
    def heal(self):
        pydirectinput.keyDown('r')
        time.sleep(0.01)
        pydirectinput.keyUp('r')
        pydirectinput.keyDown('s')
        time.sleep(1.8)
        pydirectinput.keyUp('s')
    
    #add mana functionality

    def activateRannAI(self):
        while(not self.stopFlag):

            i = secrets.randbelow(1001)

            if(i >= 0 and i <= 30):
                self.moveBackw() 
                print("moves back")
                continue
            elif(i > 30 and i <= 130):
                self.moveForw()
                print("moves forward")
                continue
            elif(i > 130 and i <= 160):
                self.moveRight()
                print("moves right")
                continue
            elif(i > 160 and i <= 190):
                self.moveLeft()
                print("moves left")
                continue
            elif(i > 190 and i <= 220):
                self.rollBack()
                print("rollsback")
                continue
            elif(i > 220 and i <= 340):
                self.rollForw()
                print("roll forward")
                continue
            elif(i > 340 and i <= 400):
                self.rollRight()
                print("rolls right")
                continue
            elif(i > 400 and i <= 460):
                self.rollLeft()
                print("rolls left")
                continue
            elif(i > 460 and i <= 485):
                self.heavyAttack()
                print("heavy attack")
                continue
            elif(i > 485 and i <= 525):
                self.jumpAttack()
                print("jump attack!")
                continue
            elif(i > 525 and i <= 650):
                self.lightAtt()
                print("light attack")
                continue
            elif(i > 650 and i <= 700):
                self.rollForwAttack()
                print("roll attack")
                continue
            elif(i > 700 and i <= 780):
                self.skillAttack()
                print("skill-attack!")
                continue
            elif(i > 780 and i <= 865):
                self.doubleLight()
                print("double light attack!")
                continue
            elif(i > 865 and i <= 950):
                self.tripleLight()
                print("tripple-light-attack!")
                continue
            elif(i > 950 and i <= 1000):
                self.heal()
                print("heals!")
                continue

class Main:

    def main():

        pyautogui.PAUSE = 0.01
        ai = RannAI()
        task = Process(target=ai.activateRannAI)

        keyboard.wait('q')
        print("--------------------")
        print("RannAI 1.3 activated")
        print("--------------------")
        task.start()
        keyboard.wait('q')
        task.terminate()

    
    if __name__ == "__main__":
        main()