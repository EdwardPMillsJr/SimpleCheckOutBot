import time
from selenium import webdriver

browser = webdriver.Chrome('D:/Eddie/Documents/bestbuybot/chromedriver.exe')
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")

buyButton = False

while not buyButton:

    try:
        addtoCardBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Unable to Buy.")
        time.sleep(1)
        browser.refresh()

    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print("The GFX Card was added to Cart!")
        addToCartBtn.click()
        buyButton = True

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-secondary")
        addToCartBtn.click()