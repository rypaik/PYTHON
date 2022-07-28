from selenium import webdriver

caps = {
    'browserName': 'firefox'
}


# command_executor points to url where python should communicate with gecko driver (url where gecko driver is running)
driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    desired_capabilities=caps
)

driver.quit()



# USING TRY BLOCK and Webdriver
#driver = webdriver.Firefox()
#try:
#    # use the driver here
#finally:
#    driver.quit()



