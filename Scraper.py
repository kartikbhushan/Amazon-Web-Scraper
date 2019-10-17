import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= '#desired url of amazon product'

#gives some info about my browser MYUSERAGENT
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def check_price():
    page = requests.get(URL , headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])
    #desired price of product 
    desired_price=#put any price you want 

    #printiongn about the product details 
    print("Product Name = "+title.strip())
    print("Product Price = ₹"+str(converted_price))
    print("Desired Product Price = ₹"+str(desired_price))
    #price check condition
    if(converted_price < float(desired_price) ):
        send_mail()
        return True

def send_mail():
    #setting up a connection between my server and gmails server 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    #EHLO = Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    server.starttls()#encrypts connection
    server.ehlo()

    #logining in to the server using username and the app password made in gmail using :google app passwords
    server.login(username,password)

    subject = 'Price fell down!'
    body= 'Check the amazon link for quick access :https://www.amazon.in/Leoxsys-150Mbps-Wireless-external-LEO-HG150N/dp/B00IWT1JA6/ref=pd_sbs_147_1/258-8740647-9522322?_encoding=UTF8&pd_rd_i=B00IWT1JA6&pd_rd_r=5a4efc61-a0a3-11e9-9984-c74b6c00308f&pd_rd_w=vue4l&pd_rd_wg=vLnbT&pf_rd_p=87667aae-831c-4952-ab47-0ae2a4d747da&pf_rd_r=XTNYM351H13YTTG985RT&psc=1&refRID=XTNYM351H13YTTG985RT'

    msg = f"Subject : {subject} \n\n{body}"
    
    #replace Sender and Receiver email with the desired email id's
    server.sendmail(
        'sender_email',
        'Receiver_email',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT')
    
    #closing all the ocnnections 
    server.quit()

username='#put your email id here to login into gmail'
#suggestion create a Password for less secure apps on gmail and use it here
password="password"

while(True):
    if check_price():
        print('We have notified stopping the checking process')
        break
        #sleep for one day you can reduce time as required
    time.sleep(86400)
