from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://example.com"
output_file = "fullpage_screenshot.png"

# Setup headless Firefox
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    driver.get(url)
    # Get full page screenshot
    driver.save_screenshot(output_file)
    print(f"Screenshot saved as {output_file}")

finally:
    driver.quit()