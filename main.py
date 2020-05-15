import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, clock
from random import random
from selenium.webdriver.common.action_chains import ActionChains
from secret import username, password

class User:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com")
        sleep(6)

        cookies = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        if len(cookies) != 0:
            cookies[0].click()

        gmail_auth = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        gmail_auth.click()

        sleep(2.5)
        base_window = self.driver.window_handles[0]

        self.driver.switch_to.window(self.driver.window_handles[1])
        input_login = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        input_login.send_keys(username)
        confirm_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        confirm_button.click()
        sleep(5 + random() * 3)
        input_password = self.driver.find_elements_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        if len(input_password) == 0:
            input_password = self.driver.find_elements_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        input_password[0].send_keys(password)
        confirm_button = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        confirm_button.click()

        self.driver.switch_to.window(base_window)

        sleep(7 + random() * 5)
        popup_location = self.driver.find_elements_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        if len(popup_location) != 0:
            popup_location[0].click()
        sleep(1.5)
        popup_notifications = self.driver.find_elements_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        if len(popup_notifications) != 0:
            popup_notifications[0].click()

    def hit_likes(self):
        start = clock()
        while clock() - start <= 3600:
            sleep(random() * 3)
            try:
                like_button = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                like_button[0].click()
            except Exception:
                # try handle popup
                popup = self.driver.find_elements_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                ActionChains(self.driver).move_to_element(popup[0]).click().perform()



user = User()
user.login()
sleep(5)
user.hit_likes()
