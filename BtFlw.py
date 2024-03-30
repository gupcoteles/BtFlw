import random
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
    parser.add_argument("-pi", "--xpathid", dest="xpathId", help="allow specifying the xpath ID")
    return parser.parse_args()

args = main()

driver = webdriver.Firefox()
driver.get("https://www." + args.site)

try:
    xpathId = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, args.xpathId)))
    print("xpath id found!")

except TimeoutException:
    print("xpath id not found or timed out.")

    while True:
        tmout = input("Do you want to try again? (y/n): ")
        if tmout == "y" or "Y":
            try:
                xpathId = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, args.xpathId)))
                print("xpath id found!")
                break

            except TimeoutException:
                print("xpath id not found or timed out.")

            except NoSuchElementException:
                print("xpath id not found.")

            except Exception as e:
                print("Error:", e)

        if tmout == "n" or "N":
            break

except NoSuchElementException:
    print("xpath id not found.")

except Exception as e:
    print("Error:", e)

driver.quit()