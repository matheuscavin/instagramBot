from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, user, password):
        self.username = user
        self.password = password
        # I'm using Firefox :)
        self.driver = webdriver.Firefox(executable_path=r'C:\User\xxx\xxx\geckodriver.exe') # Put here your Geckodriver path

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/?hl=pt-br')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]

        for pic_href in pic_hrefs:
            print(pic_href)
            if '/p/' in pic_href:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.5)
                try:
                    driver.find_element_by_xpath("//span[@class='fr66n']/button[@class='wpO6b ']").click()
                    time.sleep(19)
                except Exception as e:
                    time.sleep(5)



bot = InstagramBot('username', 'password') # Put here your username and password
bot.login()
bot.like_photo('cake') # Put here an hashtag to like