from playwright.sync_api import sync_playwright

url = "https://example.com"
screenshot_file = "playwright_screenshot.png"

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    page.screenshot(path=screenshot_file, full_page=True)
    print(f"Screenshot saved as {screenshot_file}")
    browser.close()