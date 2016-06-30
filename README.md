Amazon-Product-Script
=====================
This simple script is using the [Amazon Simple Product API] (https://github.com/yoavaviram/python-amazon-simple-product-api)
to lookup a product by the ASIN tag and return the title and price.
[![Build Status](https://travis-ci.org/jesseneal/Amazon-Product-Script.svg?branch=master)](https://travis-ci.org/jesseneal/Amazon-Product-Script)

Usage
-----
Modify Amazon credentials:
	 # Amazon credentials for API and Afflite assoc tag
	 AMAZON_ACCESS_KEY = "Enter Amazon Access Key Here"
	 AMAZON_SECRET_KEY = "Enter Amazon Secret Key Here"
	 AMAZON_ASSOC_TAG = "Enter Amazon Assocaite Tag here"

	 # Credentials for Gmail acct and destination
	 USERNAME = "gmail address for example jesseneal@gmail.com"
	 PASSWORD = "gmail app password goes here" # example: ilovekitens
	 SMS = "enternumberhere.att.net" # exaample 5555555555.att.net


Getting the product info:
     #Running the function with asin as an argument 
     def product(asin):
         item = AMAZON.lookup(ItemId=asin)
		 price = item.price_and_currency[0]
		 title = item.title

	 return (price, title)
