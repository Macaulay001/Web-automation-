#automation for  lipinsky scores
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
import pyautogui

browser = webdriver.Chrome()   
browser.get('http://www.swissadme.ch/')
elem = browser.find_element_by_xpath('//*[@id="smiles"]')
#open and read csv file
with open('test2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        pyautogui.tripleClick(852,815)
        time.sleep(3)
        pyautogui.typewrite(line[2])
        # browser.get('http://www.swissadme.ch/')
        # elem = browser.find_element_by_xpath('//*[@id="smiles"]')
        # elem.send_keys(line[2])
        send = browser.find_element_by_xpath('//*[@id="submitButton"]')
        send.click()
        time.sleep(10)
    
        formula = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[2]/td[2]').text
        molecular_weight = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[3]/td[2]').text
        hbond_acceptors = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[8]/td[2]').text
        hbond_donors = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[9]/td[2]').text
        lipinsky = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[22]/td[2]').text
        ghose  = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[23]/td[2]').text
        veber = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[24]/td[2]').text
        egan = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[25]/td[2]').text
        muegge = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[26]/td[2]').text
        bioavalability = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[27]/td[2]').text
         #save output as text file
        with open('test1.txt', 'a') as f:
            f.write(line[0])
            f.write(',')
            f.write(line[1])
            f.write(',')
            f.write(line[2])
            f.write(',')
            f.write(formula)
            f.write(',')
            f.write(molecular_weight)
            f.write(',')
            f.write(hbond_acceptors)
            f.write(',')
            f.write(hbond_donors)
            f.write(',')
            f.write(lipinsky)
            f.write(',')
            f.write(ghose)
            f.write(',')
            f.write(veber)
            f.write(',')
            f.write(egan)
            f.write(',')
            f.write(muegge)
            f.write(',')
            f.write(bioavalability)
            f.write('\n')
