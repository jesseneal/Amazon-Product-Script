## Amazon-Product-Script
-----
This simple script is using the [Amazon Simple Product API](https://github.com/yoavaviram/python-amazon-simple-product-api)
to lookup a product by the ASIN tag which returns the title and price and sends a SMS to a mobile number.

### Usage
-----
#### Install dependancies
```
pip3 install -r requirements.txt
```

#### Modify Amazon credentials:
```	 
# Amazon credentials for API and Afflite assoc tag
AMAZON_ACCESS_KEY = "Enter Amazon Access Key Here"
AMAZON_SECRET_KEY = "Enter Amazon Secret Key Here"
AMAZON_ASSOC_TAG = "Enter Amazon Assocaite Tag here"
```
#### Modify email credentials:
```	 
# Credentials for Gmail acct and destination
USERNAME = "gmail address for example jesseneal@gmail.com"
PASSWORD = "gmail app password goes here" # example: ilovekittens
SMS = "enternumberhere.att.net" # exaample 5555555555.att.net
```

#### Passing product into the function:
```     
def product(asin):
    item = AMAZON.lookup(ItemId=asin)
    price = item.price_and_currency[0] # Only return price not currency
    title = item.title

    return (price, title)

# Calling the product function and passing in the amazon ASIN product key
product_price, product_title = product('B01F2R9WV8')
```

#### Run
```
python3 amazonapi.py
```
