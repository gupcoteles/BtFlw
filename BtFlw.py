import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from assets.font.font import *
import argparse

print((random.choice(Font)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--site", dest="site", help="access the site")
    parser.add_argument("-p", "--xpathid", dest="xpathId", help="allow specifying the xpath ID")
    parser.add_argument("-b", "--browser", dest="browser", help="Use to set browser(firefox/chrome/edge)")
    return parser.parse_args()

args = main()


if args.browser == "firefox":
    driver = webdriver.Firefox()

if args.browser == "chrome":
    driver = webdriver.Chrome()

if args.browser == "edge":
    driver = webdriver.Edge()

driver.get("https://www." + args.site)

try:
    driver.find_element(By.XPATH, ("" + args.xpathId + ""))
    print("Xpath id found!")

except TimeoutException:
    print("Xpath id not found or timed out.")

    while True:
        tmout = input("Do you want to try again? (y/n): ")
        if tmout == "y" or "Y":
            try:
                driver.find_element(By.XPATH, ("" + args.xpathId + ""))
                print("Xpath id found!")
                time.sleep(1.5)
                break

            except TimeoutException:
                print("Xpath id not found or timed out.")

            except NoSuchElementException:
                print("Xpath id not found.")

            except Exception as e:
                print("Error:", e)

        if tmout == "n" or "N":
            break

except NoSuchElementException:
    print("Xpath id not found.")

except Exception as e:
    print("Error:", e)

driver.quit()