from selenium import webdriver
from selenium.webdriver.common.by import By


# found_element = locator_strategy + selector
# 5 Builtin Locator Strategies in Selenium
# By.CSS_SELECTOR
# By.TAG_NAME
# By.LINK_TEXT
# By.PARTIAL_LINK_TEXT  #USED FOR LINKS WITH DYNAMICALLY GENEREATED INFO IN LINK
# By.XPATH

# ELEMNT SELECTORS


driver = webdriver.Firefox()
try:
    driver.get('https://the-internet.herokuapp.com')

    driver.find_element(By.LINK_TEXT, 'Form Authentication')

    
    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'There were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME, 'foo')
    print(f'There were {len(els)} foo elements')
    
#    els_partial_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "me!")
#    print(f'There were {len(els_partial_link)} me elements')
#
#    els_xpath = driver.find_elements(By.XPATH, "//a[contains(@href, "site.com")]
#    els_xpath2 = dirver.find_elemtents(By.XPATH, "//div[@class="menu"]/ul/li[3]")

#    el = driver.find_element(By.CSS_SELECTOR, '#loginField')

finally:
    driver.quit()
