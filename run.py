from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from urllib.parse import urljoin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json
import os
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

class QuotesScraper:
    """The main class QuotesScraper responsible for scraping quotes from a website.
    The class is initialized without any arguments. It uses an input URL and output file location defined in a .env file.
    """

    def __init__(self):
        """Initialize QuotesScraper with default values."""
        webdriver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=webdriver_service)
        self.load_env_vars()

    def load_env_vars(self):
        """Load environment variables from .env file.
        The following environment variables are expected:
        - INPUT_URL: The URL of the website to be scraped.
        - OUTPUT_FILE: The path to the file where the scraped data should be saved.
        """
        load_dotenv()
        self.input_url = os.getenv('INPUT_URL')
        self.output_file = os.getenv('OUTPUT_FILE')

    def scrape_page(self): 
        """Scrape the given page for quotes.
        The method uses BeautifulSoup to parse the page content.
        The quotes are extracted from the parsed content and returned as a list.
        Returns:
            list: A list of the quotes scraped from the page.
        """
        logging.info("Scraping page.")
        page_content = self.driver.page_source
        return json.loads(bs(page_content, 'lxml').find_all('script')[1].text.split('for (var i in data)')[0].split('var data =')[-1].strip().rstrip(';'))

    def get_next_page(self):
        """Find the link to the next page.
        Returns:
            str: The URL of the next page, or None if this is the last page.
        """
        next_page = bs(self.driver.page_source, 'lxml').find('li', {'class': 'next'})
        if next_page:
            return urljoin(self.input_url, next_page.find('a').get('href'))
        else:
            return None

    def scrape_quotes(self):
        """Scrape all pages of the website for quotes.
        The method starts with the INPUT_URL and repeatedly calls scrape_page for the next page
        until all pages have been scraped.
        Returns:
            list: A list of all the quotes scraped from the website.
        """
        url = self.input_url
        all_quotes = []
        while url:
            logging.info(f"Fetching page: {url}")
            self.driver.get(url)
            all_quotes.extend(self.scrape_page())

            url = self.get_next_page()

        return all_quotes

    def write_quotes_to_file(self, quotes):
        """Save the scraped quotes to a file.
        The scraped quotes are saved in JSON format to the file at the path defined in OUTPUT_FILE.
        Args:
            quotes (list): The quotes to be saved.
        """
        with open(self.output_file, mode='w') as f:
            json.dump(quotes, f)

    def run(self):
        """Main execution method.
        This method scrapes all quotes from the website and then saves them to a file.
        """
        quotes = self.scrape_quotes()
        self.write_quotes_to_file(quotes)
        self.driver.quit()

if __name__ == "__main__":
    """Entry point of the script.
    When the script is run, an instance of QuotesScraper is created and run.
    """
    scraper = QuotesScraper()
    scraper.run()
