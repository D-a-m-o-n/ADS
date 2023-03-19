# # # # # # from selenium import webdriver

# # # # # # # PATH = "C:\Program Files (x86)\chromedriver.exe"
# # # # # # url = 'https://cjdropshipping.com/product/silicone-grip-device-finger-exercise-stretcher-finger-gripper-strength-trainer-strengthen-rehabilitation-training-p-1614453269613522944.html?from=HTP'

# # # # # # driver = webdriver.Chrome()
# # # # # # driver.get(url)



# # # # # # des = driver.find_element('pd-des-p ng-scope')

# # # # # # for di in des:
# # # # # #     dii = des.find_element_by_xpath('.//*[@id="pd-description"]').text
# # # # # #     print(dii)

# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.common.by import By

# # # # # # Start a new instance of the Firefox driver
# # # # # driver = webdriver.Chrome()

# # # # # # Navigate to the CJDropshipping website
# # # # # driver.get("https://cjdropshipping.com/")

# # # # # # Find the product description element on the page
# # # # # product_desc_elem = driver.find_element(By.XPATH, '//div[@class="product-desc"]')

# # # # # # Get the text of the product description element
# # # # # product_desc = product_desc_elem.text

# # # # # # Print the product description
# # # # # print(product_desc)

# # # # # # Close the browser window
# # # # # driver.quit()

# # # # # Python program to demonstrate
# # # # # # selenium

# # # # # # import webdriver
# # # # # from selenium import webdriver

# # # # # # create webdriver object
# # # # # driver = webdriver.Chrome()

# # # # # # enter keyword to search
# # # # # # keyword = ""

# # # # # # get geeksforgeeks.org
# # # # # driver.get("https://cjdropshipping.com/product/silicone-grip-device-finger-exercise-stretcher-finger-gripper-strength-trainer-strengthen-rehabilitation-training-p-1614453269613522944.html?from=HTP")

# # # # # # get element
# # # # # element = driver.find_element("ng-if","isDescription")

# # # # # # print complete element
# # # # # print(element)

# # # # # Python program to demonstrate
# # # # # selenium

# # # # # import webdriver
# # # # from selenium import webdriver

# # # # # create webdriver object
# # # # driver = webdriver.Chrome()

# # # # # enter keyword to search


# # # # # get geeksforgeeks.org
# # # # driver.get("https://cjdropshipping.com/product/silicone-grip-device-finger-exercise-stretcher-finger-gripper-strength-trainer-strengthen-rehabilitation-training-p-1614453269613522944.html?from=HTP")

# # # # # get element
# # # # element = driver.find_element_by_class_name("pd-mid-info").getText()

# # # # # print complete element
# # # # print(element)
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By

# # # # Start a new instance of the Firefox driver
# # # driver = webdriver.Chrome()

# # # # Navigate to the CJDropshipping website
# # # driver.get("https://cjdropshipping.com/")

# # # # Find the product description element on the page
# # # product_desc_elem = driver.find_element(By.XPATH, '//div[@class="product-desc"]').text

# # # # Get the text of the product description element
# # # product_desc = product_desc_elem.text

# # # # Print the product description
# # # print(type(product_desc))

# # # # Close the browser window
# # # driver.quit()
# # # Python program to demonstrate
# # # selenium

# # # import webdriver
# # from selenium import webdriver

# # # create webdriver object
# # driver = webdriver.Chrome()

# # # enter keyword to search


# # # get geeksforgeeks.org
# # driver.get("https://cjdropshipping.com/product/silicone-grip-device-finger-exercise-stretcher-finger-gripper-strength-trainer-strengthen-rehabilitation-training-p-1614453269613522944.html?from=HTP")

# # # get element
# # element = driver.find_element_by_tag_name("p")

# # # print complete element
# # print(element)
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Start a new instance of the Firefox driver
# driver = webdriver.Chrome()

# # Navigate to the CJDropshipping website
# driver.get("https://cjdropshipping.com/product/silicone-grip-device-finger-exercise-stretcher-finger-gripper-strength-trainer-strengthen-rehabilitation-training-p-1614453269613522944.html?from=HTP")

# # Find all elements containing product shipping dates on the page
# shipping_date_elems = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/pro-detail/div[1]/div[2]/div[4]/div[2]/div[1]/div')

# # Extract the text of each element and store it in a list
# shipping_dates = [elem.text for elem in shipping_date_elems]

# # Print the list of shipping dates
# print(shipping_dates)

# # Close the browser window
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By


# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://cjdropshipping.com/product/silicone-grip-device-finger-exercise-stretcher-finger-gripper-strength-trainer-strengthen-rehabilitation-training-p-1614453269613522944.html?from=HTP")

# Find the element that contains the title of the product
title_element = driver.find_element(By.CSS_SELECTOR, 'div > div > div > div > div > div > pro-detail > div').get_attribute("textContent")
print(title_element)
# Extract the text from the element
title = title_element.text

# Print the title
print(title)

# Close the driver
driver.quit()