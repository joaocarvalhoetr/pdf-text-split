import os
import csv

# Read the pdf file
from pdfminer.high_level import extract_text

from pdfminer.high_level import extract_text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

text = extract_text('abraBAL.pdf')

# Divide the text into parts of 1499 words
text = text.split()
text = [text[i:i + 1499] for i in range(0, len(text), 1499)]

# Access a website, insert the text into the field and click the button
driver = webdriver.Chrome()
driver.get("https://writer.com/ai-content-detector/")
driver.maximize_window()
driver.implicitly_wait(3)

# For each part of the text, insert it into the field name="inputs" and class="ai_textbox" and click the button type="submit" and class="dc-btn-gradient ai-content-detector-submit"

for i in range(len(text)):

    driver.find_element_by_name("inputs").clear()
    driver.find_element_by_name("inputs").send_keys(text[i])
    driver.find_element_by_class_name("ai_textbox").click()
    driver.find_element_by_class_name("dc-btn-gradient").click()

    # Wait until the text is generated
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "ai-content-detector-result")))

    # Get the text
    text_generated = driver.find_element_by_class_name("ai-content-detector-result").text

    # Write the text in a csv file
    with open('text.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text_generated])

    # Click the button type="button" and class="dc-btn-gradient ai-content-detector-reset"
    driver.find_element_by_class_name("dc-btn-gradient").click()

# Close the browser
driver.quit()



