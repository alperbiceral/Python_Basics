from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_path = "C:\Program Files\chromedriver.exe"
brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

driver.get("https://play2048.co/")
new_game = driver.find_element(by=By.CLASS_NAME, value="restart-button")
new_game.click()

game_container = driver.find_element(by=By.TAG_NAME, value="html")

while True:
    game_container.send_keys(Keys.UP)
    game_container.send_keys(Keys.RIGHT)
    game_container.send_keys(Keys.DOWN)
    game_container.send_keys(Keys.LEFT)

driver.quit()
