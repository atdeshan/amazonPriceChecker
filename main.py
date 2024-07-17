import bs4
import requests
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
username = os.getenv("username")
appPassword = os.getenv("password")
def sendEmail():

    
    with smtplib.SMTP("smtp.gmail.com") as gmail:
        gmail.starttls()
        gmail.login(user=username,password=appPassword)
        gmail.sendmail(from_addr=username,to_addrs="tharindudeshan325@gmail.com",msg=f"Subject:Price has dropped\nMacbook pro price has dropped.\ncheck:https://www.amazon.com/Apple-2024-MacBook-15-inch-Laptop/dp/B0CX235DJ6/ref=sr_1_1?crid=GQRFKO6DIAC5&dib=eyJ2IjoiMSJ9.C9sC0NE8hp3nyJDo9MaeXeNasezlFr1bXB4-B-lYmP_Zz-U9fFU1R-VdIjtExzzxC7zxYAxg6-HzcAdihsaLmZTojUeiYpCH83hcr2Nen15pmWOZ92dpcFb8BXCqI9nvuXP1dt8ZjbnUtmh_taGzS9anYQI--GtfEz0yDYCruomY23Twxs6jn_tKYkqWXqq6baB2_8yKCNbdLU8SGooY-XJPep-S3S3_kbaynJhBOuM.88KajitOU3fRdotib-OpZLCpvm45cRTJg8WSbfRgajQ&dib_tag=se&keywords=macbook&qid=1721135600&sprefix=mac%2Caps%2C1391&sr=8-1")    

webRequest = requests.get("https://www.amazon.com/Apple-2024-MacBook-15-inch-Laptop/dp/B0CX235DJ6/ref=sr_1_1?crid=GQRFKO6DIAC5&dib=eyJ2IjoiMSJ9.C9sC0NE8hp3nyJDo9MaeXeNasezlFr1bXB4-B-lYmP_Zz-U9fFU1R-VdIjtExzzxC7zxYAxg6-HzcAdihsaLmZTojUeiYpCH83hcr2Nen15pmWOZ92dpcFb8BXCqI9nvuXP1dt8ZjbnUtmh_taGzS9anYQI--GtfEz0yDYCruomY23Twxs6jn_tKYkqWXqq6baB2_8yKCNbdLU8SGooY-XJPep-S3S3_kbaynJhBOuM.88KajitOU3fRdotib-OpZLCpvm45cRTJg8WSbfRgajQ&dib_tag=se&keywords=macbook&qid=1721135600&sprefix=mac%2Caps%2C1391&sr=8-1")
soup = bs4.BeautifulSoup(webRequest.text,"html.parser")
price =soup.find(name="span",class_="a-offscreen").getText()
price = price[1:]
price = float(price.replace(",",""))
userPrice = 1000.0
if(userPrice>price):
    sendEmail()
