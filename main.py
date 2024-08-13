from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# fill in the blanks with your account information
X_USERNAME = ""
X_EMAIL = ""
X_PASSWORD = ""
TWEET = ""

class InternetSpeedXBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        sleep(4)
        emailInput = self.driver.find_element(By.XPATH, '//input[@type="text" and @name="text" and contains(@class, "r-30o5oe")]')
        emailInput.send_keys(X_EMAIL)

        sleep(2)
        nextButton = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        nextButton.click()

        sleep(2)
        usernameInput = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        usernameInput.click()
        usernameInput.send_keys(X_USERNAME)
        

        sleep(2)
        nextButton2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        nextButton2.click()
        
        sleep(2)
        passwordInput = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwordInput.send_keys(X_PASSWORD)
        loginButton = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        loginButton.click()
        
        sleep(5)
        tweetInput = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span')
        tweetInput.send_keys(TWEET)

        sleep(2)
        postButton = self.driver.find_element(By.XPATH, '//button[@data-testid="tweetButtonInline"]')
        postButton.click()

bot = InternetSpeedXBot()
bot.tweet_at_provider()    