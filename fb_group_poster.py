import subprocess
from playwright.sync_api import sync_playwright

command = '"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-session-restore'
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Start a new session with Playwright using the sync_playwright function.
with sync_playwright() as playwright:
    # Connect to an existing instance of Chrome using the connect_over_cdp method.
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")

    # Retrieve the first context of the browser.
    default_context = browser.contexts[0]

    # Retrieve the first page in the context.
    page = default_context.pages[0]

    page.goto("https://www.facebook.com/groups/5511711472209823")
    
    # click group input
    span_selector = 'span:has-text("Write something...")'
    page.wait_for_selector(span_selector)
    page.click(span_selector)
    
    # click active element and write text
    div_selector = 'div:has-text("Create a public post…")'
    page.wait_for_selector(div_selector)
    page.click(div_selector)
    page.keyboard.type("dont be geh")
    
    
    photo_button_selector = '[aria-label="Photo/video"]'
    page.wait_for_selector(photo_button_selector)
    page.click(photo_button_selector)
    
    # Select the file input element
    file_input_selector = page.locator('input[type="file"][multiple]')
    # page.wait_for_selector(file_input_selector)
    image_path = ['C:\\Users\\syahm\\Pictures\\hatsu\\hatsu14.jpg', 'C:\\Users\\syahm\\Pictures\\hatsu\\hatsu9.jpg']
    file_input_selector.set_input_files(image_path)
    page.wait_for_selector('[aria-label="Post"]')
    # page.set_input_files(file_input_selector, image_path)
    
    
    # click post button
    # element_selector = '[aria-label="Post"]'
    # page.wait_for_selector(element_selector)
    # page.click(element_selector)
    
    input("finish")
    
    browser.close()