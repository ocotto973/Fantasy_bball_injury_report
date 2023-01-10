from bs4 import BeautifulSoup
import requests
import re

from email.message import EmailMessage

import ssl
import smtplib

page = requests.get("https://www.espn.com/nba/injuries")
soup = BeautifulSoup(page.text,"html.parser")
injuryReport = soup.findAll("a",attrs={"class":"AnchorLink"})

def getReport(team):
    arr = []
    count = 0
    for i in zip(injuryReport):
        for player in team:
            if count == len(team):
                break
            if team[count] == i[0].text:
                
                if team[count] in arr:
                    continue
                else:
                    arr.append(team[count])
            else:
                count+=1
        count = 0
    report = ""
    for x in arr:
        report += (x + " is hurt" +"\n")
    return report
        
team = ["Trae Young","Malcolm Brogdon","Lonnie Walker IV","Bol Bol","Deandre Ayton",
        "RJ Barrett", "Paolo Banchero", "Jayson Tatum", "Julius Randle",
        "Bojan Bogdanovic", "Jimmy Butler", "Jusuf Nurkic", "Jaden Mcdaniels",
        "Tyrese Maxey"]
#print (getReport(team))
report = getReport(team)
email_sender = 'ENTER YOUR EMAIL'
email_password = 'YOUR PASSWORD'
email_receiver = 'lowopes304@webonoid.com' #receiving email
subject = "Fantasy Injury Report"
body = "Your report is showing that:" + "\n" + getReport(team)
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())

