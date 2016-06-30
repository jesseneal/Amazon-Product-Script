#!/usr/bin/python

from amazon.api import AmazonAPI
import smtplib

# Amazon crentials for API and Afflite assoc tag
AMAZON_ACCESS_KEY = "Enter Amazon Access Key Here"
AMAZON_SECRET_KEY = "Enter Amazon Secret Key Here"
AMAZON_ASSOC_TAG = "Enter Amazon Assocaite Tag here"

# Credentials for Gmail acct and destination
USERNAME = "gmail address for example jesseneal@gmail.com"
PASSWORD = "gmail app password goes here" # example: ilovekitens
SMS = "enternumberhere.att.net" # exaample 5555555555.att.net

# Assigning Amazon creds to the API
AMAZON = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

# Running the function with asin as an argument 
def product(asin):
    item = AMAZON.lookup(ItemId=asin)
    price = item.price_and_currency[0] # Only return price not currency
    title = item.title

    return (price, title)

# Calling the product function and passing in the amazon ASIN product key
product_price, product_title = product('B01F2R9WV8')

# Budling gmail smtp and sending the text
if product_price <= 15.00:
    try:
        text_msg = "The current price of {0} is {1}".format(product_title, str(product_price))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(USERNAME,PASSWORD)
        server.sendmail(USERNAME, SMS, text_msg)
        server.quit()
    except Exception,e:
        print "Something went wrong {0}".format(e)


