from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('/Users/estvorogov/Desktop/stepik/Selenium/chromedriver')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://passport.yandex.ru/auth?mode=add-user&retpath=%2F%2Fyandex.ru%2Fsupport%2Fid%2Fauth.html'
driver.get(base_url)
driver.maximize_window()


def click(xpath):
    click_1 = driver.find_element(By.XPATH, xpath)
    click_1.click()


def send_text(text, xpath):
    text_in = driver.find_element(By.XPATH, xpath)
    text_in.clear()
    text_in.send_keys(text)


def double_click(xpath):
    action = ActionChains(driver)
    new_push = driver.find_element(By.XPATH, xpath)
    action.double_click(new_push).perform()


send_text('lisasumina@yandex.ru', '//*[@id="passp-field-login"]')
click('//*[@id="passp:sign-in"]')
send_text('Qwerty218805', '//*[@id="passp-field-passwd"]')
click('//*[@id="passp:sign-in"]')
time.sleep(3)

base_url_2 = 'https://disk.yandex.ru/client/disk'
driver.get(base_url_2)
time.sleep(5)

click("//*[@id='app']/div/div/div[3]/div[1]/div[1]/div/div/span[2]/button")
click('//*[@id="nb-1"]/body/div[3]/div/button[1]/span[1]')
send_text(
    'Test', '//*[@id="nb-1"]/body/div[4]/div[2]/div/div/div/div/div/div[1]/div/form/span/input')
click('//*[@id="nb-1"]/body/div[4]/div[2]/div/div/div/div/div/div[2]/button')
time.sleep(3)

double_click(
    '//*[@id="app"]/div/div/div[3]/div[2]/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div')
time.sleep(2)
click('//*[@id="app"]/div/div/div[3]/div[1]/div[1]/div/div/span[2]/button')
click('//*[@id="nb-1"]/body/div[3]/div/button[3]/span[1]')
time.sleep(1)
send_text(
    'Fail', '//*[@id="nb-1"]/body/div[4]/div[2]/div/div/div/div/div/div[1]/div/form/span/input')
click('//*[@id="nb-1"]/body/div[4]/div[2]/div/div/div/div/div/div[2]/button')
time.sleep(10)

return_folder = 'https://disk.yandex.ru/client/disk/Test'
driver.get(return_folder)
