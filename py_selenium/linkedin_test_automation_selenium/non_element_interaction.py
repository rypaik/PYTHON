from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
finally:
    driver.quit()

# BROWSER ACTIONS
# got forward and back in browser history
driver.back()
driver.forward()

# refresh page
driver.refresh()

# get current html source as string
source = drive.page_source

# execute javascript in the context of the page and get the result
res = driver.execute_script('return 2+2;')

# save a screenshot of th ecurrent state of the page to a file
driver.save_screenshot('foo.png')


# WINDOWS FRAMES ALERTS
# Window Interaction
# Get a list of IDs for all available windowss
name_list = diver.window_handles

# Switch to a given window by its handle
driver.switch_to.window(handle)

# Get the handle of currently active window
handle = driver.current_window_handle

# Max and Min window
driver.maximize_window()
driver.minimize_window()
#get width, height and x & y position of the window
driver.get_window_rect()

# set widthm height and position of window
driver.set_window_rect(x=50, y=50, height=100, width=200)

# FRAME INTERACTION
# switch to a given frame, either by its index, its name, or as a found WebElement
driver.switch_to.frame(frame)

# swithc focus to parent of current frame
driver.switch_to.parent_frame()
driver.siwtch_to.default_content()


