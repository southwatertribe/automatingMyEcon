import time
import winsound
import logging
# <div id="qf1" class="shiny-text-output shiny-bound-output" aria-live="polite">The answer is not correct. Try again!</div>

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys

service = Service("C:\chromedriver.exe")

service.start()

driver = webdriver.Remote(service.service_url)

# Gets the link and opens a chrome page
driver.get('http://hhsievertsen.shinyapps.io/Economic_data_202122_Quiz/')

# Vars
ans = 101000
myId = 2207234
questionSelector = driver.find_element_by_link_text("Question 9")
studentIDEnter = driver.find_element_by_id("studentid")
answerfield = driver.find_element_by_id("qa9")
answerSubmitButton = driver.find_element_by_id("qb9")
solved = False

# functions
questionSelector.click()

studentIDEnter.send_keys(myId)

studentIDEnter.send_keys(Keys.DELETE)

answerfield.send_keys(ans)

answerSubmitButton.click()

time.sleep(1.5)

# This is the element change to check every loop for a change ofa answer
element = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/div[2]/div/div[9]/div[3]').text

print(element)

# Loop to increment and check answer
while solved == False:
    if element == "The answer is not correct. Try again!":
        ans += 1
        answerfield.click()
        answerfield.clear()
        #ans = round(ans, 2)
        answerfield.send_keys(ans)
        answerSubmitButton.click()
        time.sleep(0.2)
        element = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div[9]/div[3]').text
    else:
        solved = True
        # Beep and stop when the right answer is found, so I can do other stuff in the meantime :)
        winsound.Beep(440, 500)
# need a small delay for every test
time.sleep(500)

driver.quit()


# q 8 /html/body/div[1]/div/div[1]/div/div[2]/div/div[8]/div[3] <--This element should be changed for each question attempted
