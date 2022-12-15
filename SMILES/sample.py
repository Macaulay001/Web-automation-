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

send = browser.find_element_by_xpath('//*[@id="myHeader1"]')
send.click()
time.sleep(6)
selk = browser.find_element_by_xpath('//*[@id="smiles"]')
selk.click()
time.sleep(6)
smils = browser.find_element_by_xpath('//*[@id="smi"]')
smils.send_keys('CC(C)CCCC(C)C1CCC2C1(CCC3C2CC=C4C3(CCC(C4)O)C)C')
time.sleep(3)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(30)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(8)
#1st
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('Cholesterol synthesis inhibitor')
pyautogui.press('enter')
time.sleep(2)
pyautogui.doubleClick(471,829)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
# pyautogui.write(line[0])
pyautogui.write(',Cholesterol,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(532,828)
time.sleep(1)
pyautogui.doubleClick(532,828)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Pj,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)


#2nd
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('Hypolipemic')
pyautogui.press('enter')
time.sleep(3)
pyautogui.doubleClick(471,829)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Hypolipemic,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)
time.sleep(1)
pyautogui.doubleClick(532,828)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Pj,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)

#3rd
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('HMG CoA synthase inhibitor')
pyautogui.press('enter')
time.sleep(3)
pyautogui.doubleClick(471,829)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', HMGS,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)
time.sleep(1)
pyautogui.doubleClick(532,828)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Pj,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)
time.sleep(2)

#4th
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('Hypolipemic')
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('Cholesterol synthesis inhibitor')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('HMG CoA reductase inhibitor')
pyautogui.press('enter')
time.sleep(3)
pyautogui.doubleClick(471,829)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', HMGR,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)
time.sleep(1)
pyautogui.doubleClick(532,828)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Pj,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
# pyautogui.click(289,615)
# pyautogui.scroll(50000)
pyautogui.click(289,615)
time.sleep(2)




#5th
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('Cardioprotectant')
pyautogui.press('enter')
time.sleep(3)
pyautogui.doubleClick(471,829)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Cardio,')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(289,615)
time.sleep(1)
pyautogui.doubleClick(532,828)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.click(1656,32)
pyautogui.write(', Pj,')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(289,615)
time.sleep(2)
pyautogui.hotkey('ctrl', 'f')
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.click(289,615)
time.sleep(3)







        


























