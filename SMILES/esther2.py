from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time

browser = webdriver.Chrome()   


with open('canonical.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        browser.get('http://www.swissadme.ch/')
        elem = browser.find_element_by_xpath('//*[@id="smiles"]')
        elem.send_keys(line[1])
        send = browser.find_element_by_xpath('//*[@id="submitButton"]')
        send.click()
        time.sleep(10)

        # lipinsky = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[22]/td[2]') 
        # print(lipinsky)
        lipinsky = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[22]/td[2]').text
        bioavalability = browser.find_element_by_xpath('//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[27]/td[2]').text
        print(lipinsky)
        with open('esther.txt', 'a') as f:
            f.write(line[0])
            f.write(' ')
            f.write(lipinsky)
            f.write('   ')
            f.write('bioavalability')
            f.write(' ')
            f.write('score')
            f.write(' ')
            f.write(bioavalability)
            f.write('\n')
        # with open('esther.txt', 'a') as f:
        #     f.write('\n'.join(line[0]))
        #     f.write('\n'.join(lipinsky))