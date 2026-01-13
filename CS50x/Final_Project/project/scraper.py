from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

class Scraper():
    def __init__(self, headless):
        options = Options()
        if headless:
            options.add_argument('--headless')  # Run in headless mode
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')  # Set window size to avoid layout issues

        self.driver = webdriver.Chrome(options=options)
        self.data = []

    def scrape_page(self, url):
        last = url.split('/')[-1]
        if last == '':
            url += 'videos'
        elif last != 'videos':
            url += '/videos'
        
        self.driver.get(url)
        self.driver.implicitly_wait(2)
        self.scrape()

    def scrape(self):
        i = 1  # Skip header
        n = 39

        # Print header
        text = 'YouTube Scraper'
        print('-' * n)
        print(f'| {text.center(n - 4)} |')
        print('-' * n)

        while True:
            self.driver.execute_script("window.scrollBy(0, 200);")
            vids = self.driver.find_elements(By.ID, 'content')

            if i >= len(vids):
                self.driver.execute_script("window.scrollBy(0, 200);")
                time.sleep(2)
                new_vids = self.driver.find_elements(By.ID, 'content')

                if len(new_vids) == len(vids):
                    # Print summary
                    text1 = 'Scraping completed.'
                    text2 = f'Total videos scraped: {i}'
                    print('-' * n)
                    print(f'| {text1.center(n - 4)} |')
                    print(f'| {text2.center(n - 4)} |')
                    print('-' * n)

                    break  # No more new videos
                continue  # Retry with updated vids

            try:
                vid = vids[i]
                info = {}

                info['Thumbnail'] = vid.find_element(By.XPATH, './/img').get_attribute('src')
                info['Title'] = vid.find_element(By.XPATH, './/h3').text
                info['Duration'] = vid.find_element(By.ID, 'overlays').text
                views, posted = vid.find_elements(By.XPATH, './/div[@id="metadata-line"]//span')
                info['Views'], info['Posted'] = views.text.replace(' views', ''), posted.text

                text = f'Suceesfully scraped video #{i}'
                print(f"| {text.center(n - 4)} |")

                self.data.append(info)
                i += 1  # Move on to next vid

            except Exception as e:
                print(f"Error {e}. Retrying video {i}...")
                time.sleep(1)
                continue  # Reattempt current video

    def export_to_csv(self, file_name):
        df = pd.DataFrame(self.data)
        df.index += 1
        df.to_csv(file_name, index=True)

# For debug
if __name__ == '__main__':
    scraper = Scraper(headless=True)
    scraper.scrape_page('https://www.youtube.com/@symphez/videos')
    scraper.export_to_csv(file_name='youtube.csv')
