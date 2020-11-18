# BestBuyLink

# Search the price of a specific product daily in (amazon.in) and save it in a file.
# If the price is low when compared to the yesterday's price then send a buy link msg to the user in discord.
# If the price is high then send the difference in price in Rupees as discord msg.

import selenium
from selenium import webdriver as wb
import time

try:
    app = wb.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    url = 'https://www.amazon.in/OnePlus-Nord-Gray-256GB-Storage/dp/B08697MJD8/ref=lp_21827649031_1_1?s=electronics&ie=UTF8&qid=1605699704&sr=1-1'
    app.get(url)

    product = app.find_element_by_xpath("//span[@id='productTitle']")
    product_text = product.text
    print(product_text)

    price = app.find_element_by_xpath("//*[@id='priceblock_ourprice']")
    price_text = price.text
    print(price_text)

    search = app.find_elements_by_xpath("//*[@id='twotabsearchtextbox']").click()

except Exception as e:
    print("Exception --> ", str(e))

