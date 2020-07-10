from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.thewarehouse.pk/makeup-pouch"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(link)
while True:
    try:
        loadmore = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[class='btn show-more col-md-3 center-block btn-lg']")))
        driver.execute_script("arguments[0].click();", loadmore)
        wait.until(EC.staleness_of(loadmore))
    except Exception:break

for elems in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"btn show-more col-md-3 center-block btn-lg"))):
    print(elems.get_attribute("href"))

driver.quit()
