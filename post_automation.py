import subprocess
from playwright.sync_api import sync_playwright



class PostAutomation():
    
    def open_chrome(self):
        command = '"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-session-restore'
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    def goto_page(self, url):
        self.page.goto(url)        
            
    def click_element(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)
        
    def type_text(self, text):
        self.page.keyboard.type(text)
        
    def upload_images(self, file_input_selector, image_paths):
        file_input = self.page.locator(file_input_selector)
        file_input.set_input_files(image_paths)
        
    def close_browser(browser):
        browser.close()
        
    def post_fb_group(self, url, text, image_paths):
        self.open_chrome()
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
            default_context = browser.contexts[0]
            self.page = default_context.pages[0]
            self.goto_page(url)
            self.click_element('span:has-text("Write something...")')
            self.click_element('div:has-text("Create a public post…")')
            self.type_text(text)
            self.click_element('[aria-label="Photo/video"]')
            self.upload_images('input[type="file"][multiple]', image_paths)
            # self.click_element('[aria-label="Post"]')
            input("done")
    
    
if __name__ == "__main__":
    url = "https://www.facebook.com/groups/5511711472209823"
    text = "anything"
    image_paths = [
        'C:\\Users\\syahm\\Pictures\\hatsu\\hatsu14.jpg', 
        'C:\\Users\\syahm\\Pictures\\hatsu\\hatsu9.jpg'
        ]
    klas = PostAutomation()
    klas.post_fb_group(url, text, image_paths)
    