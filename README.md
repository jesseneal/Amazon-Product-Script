Amazon-Product-Script
=====================
This simple script is using the [Amazon Simple Product API] (https://github.com/yoavaviram/python-amazon-simple-product-api)
to lookup a product by the ASIN tag and return the title and price.

Usage
-----
    Running the function with asin as an argument 
    def product(asin):
        item = AMAZON.lookup(ItemId=asin)
        price = item.price_and_currency[0]
        title = item.title

    return (price, title)
