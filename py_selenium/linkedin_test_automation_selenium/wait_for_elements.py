from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# three waiting strategies
# Static Waiting - like python's time.sleep(x)

# Implicit Waiting - Use the Webdriver server's built-in element finding retry, up to a timeout
# when you have an implicit wait active - you request an element from the server and it can't be found, the server will keep trying to find it up until the timeout you set
# set the implicit wait timeout using - driver.implicity_wait(10)
# implicit wait timeouts are global and apply to all elements you find
# implicit waits only for for finding elements, DOES NOT work for ohter kind fo app states( like text values for elements, and page titles)


# Explicit Waiting - Use Expected Conditions to poll the app for appropriate state



# EXPLICIT WAITS
# pool for appsatate using client side methods
# Can check fo any state wich can be determined using Webdriver functionality
# polling builtin to th epython client on a class classed WebDriverWait ( selenium.webdriver.support.wait.WebDriverWait)
# WebDriverWaits have an until() method whic takes an Expected Condition
# (selenium.webdriver.support.expected_conditions)

# samples of expected conditions
expected_conditions.title_is('some title')
expected_conditions.url_to_be('https://some.url.com')
expected_conditions.presence_of_element_located(By,CSS_SELECTOR, '#foo'))




  
driver = webdriver.Firefox()
try:
    # passing in driver, and timeout time (this is 10 secs)
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    # Explicit wait
    # wait.until(expected_conditions.presence_of_element_located()
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))

# throws a TimeoutException
# TODO: Can a TimeoutException be logged in loguru or pytest
#    wait.until(EC.url_to_be('https://the-internet.herokuapp.com'))
#    print(driver.current_url)
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
finally:
    driver.quit()
