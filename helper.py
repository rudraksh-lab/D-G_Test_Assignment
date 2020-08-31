
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def start_up():
    global driver
    driver = webdriver.Chrome(executable_path = './chromedriver')
    driver.get("https://www.domesticandgeneral.com/products")
    driver.set_window_size(1440, 900)


def product_select(product):
    try:
        time.sleep(2)
        driver.find_element(By.ID,('Combined-Shape')).click()
    except:
        pass
    time.sleep(2)
    element = driver.find_element(By.CSS_SELECTOR, "#topCat_" + product + "> .linkContainer img")
    driver.execute_script("arguments[0].click();", element)
    if (product=="10105" or product=="10118"):
        element = driver.find_element(By.CSS_SELECTOR, "#showCategory_" + product + " .linkContainer:nth-child(2) img")
        driver.execute_script("arguments[0].click();", element)


def product_detail(brand, garantee, product):
    try:
        time.sleep(2)
        driver.find_element(By.ID,('Combined-Shape')).click()
    except:
        pass

    time.sleep(3)
    choose=driver.find_element(By.NAME,'condition')
    choose.click()
    driver.find_element(By.XPATH, "//option[. = 'good working order']").click()
    if (garantee=='still active'):
        driver.find_element(By.NAME,'guarantee').click()
        driver.find_element(By.XPATH, "//option[. = '"+garantee+"']").click()
        driver.find_element(By.XPATH, "//option[. = '2 Years']").click()

        beko=driver.find_element(By.NAME,'manufacturer')
        beko.send_keys(brand)
        beko.send_keys(Keys.ENTER)
        time.sleep(1)

        date = driver.find_element(By.NAME,'monthNyear')
        date.click()

        date.send_keys("04/07/2020")
        date.send_keys(Keys.ENTER)
        if (int(product)!=10118):
            time.sleep(1)
            driver.find_element(By.NAME,'cost').click()
            driver.find_element(By.XPATH, "//option[. = '£100 - £199']").click()

        time.sleep(1)
        driver.find_element(By.XPATH, ('//*[@id="parent_finish"]/div/input')).click()

        time.sleep(3)
    else:
        driver.find_element(By.NAME,'guarantee').click()
        driver.find_element(By.XPATH, "//option[. = '"+garantee+"']").click()

        beko=driver.find_element(By.NAME,'manufacturer')
        beko.send_keys(brand)
        beko.send_keys(Keys.ENTER)
        time.sleep(1)

        driver.find_element(By.NAME,'bought_month').click()
        driver.find_element(By.XPATH, "//option[. = 'January']").click()

        time.sleep(1)

        driver.find_element(By.ID,'bought_year').click()
        driver.find_element(By.XPATH, "//option[. = '2018']").click()

        if (int(product)!=10118):
            time.sleep(1)
            driver.find_element(By.NAME,'cost').click()
            driver.find_element(By.XPATH, "//option[. = '£100 - £199']").click()

        time.sleep(1)
        driver.find_element(By.XPATH, ('//*[@id="parent_finish"]/div/input')).click()

        time.sleep(3)


def product_basket():

    try:
        driver.find_element(By.ID,('Combined-Shape')).click()
        time.sleep(2)
    except:
        pass
    time.sleep(2)

    add=driver.find_element(By.ID,'add2CartBtn')
    driver.execute_script("arguments[0].click();", add)


    time.sleep(2)
    driver.find_element(By.ID,"viewCartButton").click()


def product_name():
    try:
        driver.find_element(By.ID,('Combined-Shape')).click()
        time.sleep(2)
    except:
        pass
    time.sleep(2)
    prodcut_name=driver.find_element(By.XPATH,'//*[@id="WC_OrderItemDetailsf_div_2_1"]/div/div[1]/p[1]/span')
    return prodcut_name.text

def product_price():
    try:
        driver.find_element(By.ID,('Combined-Shape')).click()
        time.sleep(2)
    except:
        pass
    time.sleep(2)
    price=driver.find_element(By.XPATH,'//*[@id="WC_OrderItemDetailsf_div_2_1"]/div/div[2]/p[1]/span[2]')
    return price.text

def continue_shopping():
    time.sleep(2)
    add=driver.find_element(By.XPATH,'//*[@id="basketPage"]/div[1]/div[1]/div[2]/a[2]')
    driver.execute_script("arguments[0].click();", add)
    try:
        driver.find_element(By.ID,('Combined-Shape')).click()
        time.sleep(2)
    except:
        pass
    driver.quit()
