# Web-Browser Automation with Selenium - Headspin(Appium)

[Installing Chromedriver for M1](https://www.swtestacademy.com/install-chrome-driver-on-mac/)
[chromedriver download](https://sites.google.com/chromium.org/driver/)
[Firefox geckodriver download](https://github.com/mozilla/geckodriver/releases)




Test Website
http://the-internet.herokuapp.com

[Selenium Webdriver Documentation](https://www.selenium.dev/documentation/webdriver/)

### TOC 
[01 - Introducing Website](#)
[02 - Sessions](#Sessions)
    - sessions.py
    [02b - Sessions Remote](#Sessions_remote)
    - sessions_remote.py
    [02c - Sessions with Get](#Sessions_w_Get)
    - sessions_with_get.py
[03 - Finding Web Elements](#Finding Elements)
[04 - Determining Element Selectors](#Determing)
[05 - Waiting for Elements](#### Sessions)
[07 - Interacting with Web Elements](#### Sessions)
[08 - Non-Element Interaction](#### Sessions)


------
#### Sessions
  - sessions.py
    - starting and ending sessions wiht python Gecko and Chromedrivers
    - deleting a wbedriver session
    - Translates Webdriver commands to raw http calls
    ``` html
    POST /session HTTP/1.1
    Content-Type application.json
    
    {
      "capabilities": {
        "alwaysMatch": {
          "browserName": "Firefox"
        }
      }
    }
    ```
    
**Built-In Driver Types**
webdriver.Firefox()
webdriver.Chrome()
webdriver.Safari()

#### Sessions_remote/
**Generic Webdriver**
webdriver.Remote()

- Sessions Remote - Generic Sessions
  - session_remote.py
    - Webdriver Capabilities
      - browserName
      - browserVersion
      - platformName
    - Ending Sessions
      - `quit()`


#### Sessions_w_Get
  - sessions_with_get.py


#### Finding Elements
XPath is great at looking through HTML Hierarchical Data
- Use features of Elements that are not likely to change

el = driver.find_element(strategy, selector)
  - driver.find_element() will return one element , or will raise an Exception
  - selenium.common.exceptions.NoSuchElementException

Finding Multiple Elements at once

els = driver.find_elements(strategy, selector)


find all the anchor tags on page
els = driver.find_elements(By.TAG_NAME, 'a')



#### Determining Element Selectors
-

