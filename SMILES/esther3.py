from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
browser = webdriver.Chrome()
#open and read csv file
with open('esther.csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        browser.get('https://tox-new.charite.de/protox_II/index.php?site=compound_input')
        elem = browser.find_element_by_xpath('//*[@id="smiles_field"]')
        elem.send_keys(line[3])
        send = browser.find_element_by_xpath('//*[@id="contentwrapper"]/div[4]/form/table/tbody/tr[2]/td[2]/input[2]')
        send.click()
        time.sleep(5)
        sends = browser.find_element_by_xpath('//*[@id="doodle"]/input')
        sends.click()