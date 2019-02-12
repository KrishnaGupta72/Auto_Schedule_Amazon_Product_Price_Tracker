# Amazon product price tracker using Python

# importing libraries
from requests import get
from bs4 import BeautifulSoup
import sys
import schedule
import time
#For system speaking
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

def mainprogram():
    for hit in range(5):
        url="https://www.amazon.in/Airtel-4G-Hotspot-E5573Cs-609-Portable/dp/B06WV9WR4Z"
        time.sleep(7)
        response = get(url)
        resp=response.text
        # print(len(resp))
        match_val=resp.find("Robot check") or resp.find("Robot Check") or resp.find("robot check")
        if match_val!= -1 or len(resp) > 12000:#Condition for not a captcha page
            with open("Prod_page.html",'w', encoding ='utf-8') as file:#Writing Product Page
                file.write(resp)
            # print(resp)
            html_soup = BeautifulSoup(resp,"lxml")
            price_container = html_soup.find("div", {"id":"cerberus-data-metrics"})['data-asin-price']#Capturing id's "data-asin-price" attribute value
            print(price_container)#1999.0

            # convert to integer
            current_price = int(float(price_container))
            print(current_price)
            your_price = 2300#My budget price
            if current_price <= your_price:
                # print("Price is under your budget book now...HURRY!!!")
                speak.Speak("Price is under your budget book now...HURRY!!!")

            else:
                # print("Price is not under your budget please wait for the best deal")
                speak.Speak("Price is not under your budget please wait for the best deal")

            break
        else:
            continue#Hit again for the Product page, here we are getting CAPTCHA Page

def job():
    # print("Tracking....")
    speak.Speak("Tracking....")
    mainprogram()

# main code
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)