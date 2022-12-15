from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
import pyautogui

main_page = 'https://pubchem.ncbi.nlm.nih.gov/'
browser = webdriver.Chrome()
browser.get('https://pubchem.ncbi.nlm.nih.gov/')
with open('compounds.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        pyautogui.click(237,362)
        time.sleep(10)
        # browser.get(main_page)
        # time.sleep(2)
        pyautogui.typewrite(line[0])
        pyautogui.press('enter')
        time.sleep(10)
        compound_name = browser.find_element_by_xpath('//*[@id="featured-results"]/div/div[2]/div/div[1]/div[2]/div[1]/a/span/span/span[1]').text
        time.sleep(2)
        send = browser.find_element_by_xpath('//*[@id="featured-results"]/div/div[2]/div/div[1]/div[2]/div[1]/a/span/span/span[1]')
        send.click()
        time.sleep(10)
        canonical = browser.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div[2]/div[1]/p').text
        with open('test1.txt', 'a') as f:
            f.write(line[0])
            f.write(',')
            f.write(compound_name)
            f.write(',')
            f.write(canonical)
            f.write('\n')
        # browser.quit()