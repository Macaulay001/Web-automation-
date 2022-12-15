# with open('test.tsv') as f:
#     # Read space-delimited file and replace all empty spaces by commas
#     data = f.read().replace('\t', ',')
#     # Write the CSV data in the output file
#     print(data, file=open('test1.csv', 'w'))
#automation for  pa pi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
import pyautogui

browser = webdriver.Chrome()   
browser.get('https://www.mcgill.ca/bbme/people/field_mprofile_research_areas/bioinformatics_and_computational_biology%20')
time.sleep(3)
for i in range(30):
    pyautogui.click(1562,1011)
time.sleep(3)
for i in range(30):
    pyautogui.click(1564,210)
time.sleep(2000)