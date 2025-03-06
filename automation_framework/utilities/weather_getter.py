from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def search_and_get_temp(driver, city_name):
    wait = WebDriverWait(driver, 10)

    search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class, 'picker-city__input')]")))
    search_box.send_keys(city_name)
    search_first_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='as']//ul[@class='asu']/li[1]")))
    search_first_element.click()
    temperature = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='qlook']//div[@class='h2']")))

    return int(temperature.text.split(" ")[0])