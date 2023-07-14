# extract the service address (6540 SCHMIDT LN UNIT D309, EL CERRITO, CA 94530-3271493)
# and rate name (E-1 Standard Residential Electric Service).
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_address():
    driver = webdriver.Chrome(options=Options())
    driver.get('file:///Users/sarahfloyd/Downloads/pge_meter_details.html')

    address_element = driver.find_element(By.XPATH, '//div[@class="module-body sa-info"]/ul/li[1]')
    city_state_zip_element = driver.find_element(By.XPATH, '//div[@class="module-body sa-info"]/ul/li[2]')
    rate_name_element = driver.find_element(By.XPATH, '//div[@class="module-body"]/h3')
    address = address_element.text.strip()

    city_state_zip = city_state_zip_element.text.strip()
    city, state_zip = city_state_zip.split(',', 1)
    city = city.strip()
    state_zip = state_zip.strip()
    state, zip_code = state_zip.split(' ', 1)
    zip_code = zip_code.strip()
    rate_name = rate_name_element.text.strip()

    print("Service Address:", address)
    print("City:", city)
    print("State:", state)
    print("Zip Code:", zip_code)
    print("Rate Name:", rate_name)

    driver.quit()

if __name__ == "__main__":
    get_address()

# initialize chrome driver
# get method
# file path
# find_element byxpath
# remove leading or tailing whitespace
# organize
