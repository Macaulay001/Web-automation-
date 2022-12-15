#automation for  pa pi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
import pyautogui

browser = webdriver.Chrome()   
browser.get('http://www.way2drug.com/passonline/predict.php')
elem = browser.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/div/div/div/div/form/div/p[3]/a')
elem.click()
time.sleep(4)
pyautogui.press('tab', presses=2)
pyautogui.write('oladimeji0355', interval=0.25)
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write('90fb01aae0', interval=0.25)
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(6)

with open('compoundspass.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:

        send = browser.find_element_by_xpath('//*[@id="myHeader1"]')
        send.click()
        time.sleep(3)
        selk = browser.find_element_by_xpath('//*[@id="smiles"]')
        selk.click()
        time.sleep(3)
        smils = browser.find_element_by_xpath('//*[@id="smi"]')
        smils.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        smils.send_keys(Keys.DELETE)
        time.sleep(1)
        smils.send_keys(line[1])
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(10)
        for i in range(30):
            pyautogui.click(1561,1039)
        time.sleep(3)
        for i in range(30):
            pyautogui.click(1564,210)
        time.sleep(1)

        #1st
        #notepad position
        pyautogui.click(1686,959)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(136,494)
        time.sleep(1)
        for i in range(30):
            #scroll up
            pyautogui.click(1564,210)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.doubleClick(471,628)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        #output notepad position
        pyautogui.click(1675,19)
        pyautogui.write(line[0])
        pyautogui.write(', CholesterolPa,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(532,828)
        time.sleep(1)
        pyautogui.doubleClick(530,629)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1675,19)
        pyautogui.write(', Pi,')
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(1)
        # pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(289,615)
        time.sleep(2)
        

        #2nd
        #notepad position
        pyautogui.click(1684,822)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(136,494)
        time.sleep(1)
        for i in range(30):
            #scroll up
            pyautogui.click(1564,210)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.doubleClick(471,628)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        #output notepad position
        pyautogui.click(1675,19)
        # pyautogui.write(line[0])
        pyautogui.write(', hypolipemicPa,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(532,828)
        time.sleep(1)
        pyautogui.doubleClick(530,629)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1675,19)
        pyautogui.write(', Pi,')
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(1)
        # pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(289,615)
        time.sleep(2)



        #3rd
        #notepad position
        pyautogui.click(1687,690)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(136,494)
        time.sleep(1)
        for i in range(30):
            #scroll up
            pyautogui.click(1564,210)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.doubleClick(471,628)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        #output notepad position
        pyautogui.click(1675,19)
        # pyautogui.write(line[0])
        pyautogui.write(', hmgsPa,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(532,828)
        time.sleep(1)
        pyautogui.doubleClick(530,629)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1675,19)
        pyautogui.write(', Pi,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(289,615)
        time.sleep(2)


        #4th
        #notepad position
        pyautogui.click(1690,552)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(136,494)
        time.sleep(1)
        for i in range(30):
            #scroll up
            pyautogui.click(1564,210)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.doubleClick(471,628)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        #output notepad position
        pyautogui.click(1675,19)
        # pyautogui.write(line[0])
        pyautogui.write(', cardioPa,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(532,828)
        time.sleep(1)
        pyautogui.doubleClick(530,629)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1675,19)
        pyautogui.write(', Pi,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(289,615)
        time.sleep(2)


        #5th
        #notepad position
        pyautogui.click(1693,415)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(136,494)
        time.sleep(1)
        for i in range(30):
            #scroll up
            pyautogui.click(1564,210)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.doubleClick(471,628)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        #output notepad position
        pyautogui.click(1675,19)
        # pyautogui.write(line[0])
        pyautogui.write(', hmgrPa,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.click(532,828)
        time.sleep(1)
        pyautogui.doubleClick(530,629)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1675,19)
        pyautogui.write(', Pi,')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(289,615)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.press('delete')
        time.sleep(1)
        pyautogui.click(289,615)
        time.sleep(2)


        






















