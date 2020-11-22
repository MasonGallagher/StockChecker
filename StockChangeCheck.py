"""
    Mason Gallagher's Simple Stock Scraper
    Example Values:
    url: https://www.game.co.uk/playstation-5#Page2
    element: <span class="sectionButton"><a href="javascript:void(0);">Out of stock</a></span>
    phrase: Out of stock
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import webbrowser
import re

#open the url provided and search for the phrase
def check_website(url, phrase, className, type):
    print("opening webpage")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    job_elems = soup.find_all(type, class_=className)
    found = False;
    for job_elem in job_elems:
        text = str(job_elem).lower()
        if phrase in text:
            found = True
    print("closing webpage")
    browser.close()
    return found

#Get Values
url = input("what website? ")
element = input("Paste the element ")
phrase = input("What phrase should i look for? ")

#split values pasted for class name and type
split = element.split(" >")[0]
className = re.findall(r'"([^"]*)"', split)[0]
type = split[1:element.index(" ")]

# Loop ever 10 seconds until KeyboardInterrupt(Ctrl+C) is pressed
while True:
    try:
        if check_website(url, phrase.lower(), className, type):
            print("no change")
        else:
            print("CHANGE IN PAGE, CHECK FOR STOCK")
            webbrowser.open_new(url)
            #sleep to ensure youtube autplays the noise
            time.sleep(1)
            webbrowser.open_new_tab("https://youtu.be/Cm-LyRgTYe0?t=14")
            break

        time.sleep(10)
    except KeyboardInterrupt:
        break

