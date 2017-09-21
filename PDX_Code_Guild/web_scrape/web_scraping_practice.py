'''Write a simple program using beautifulsoup4 that scrapes [Quotes to Scrape](http://quotes.toscrape.com/) and returns the top 10 tags as a list.

  2. Use the [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to gather the top 10 tags.

* Make a dictionary from the first page of quotes. Make the key the authors name and the value the quote.
* Output a new html page with your own css styling that displays the quotes and tags.'''

from bs4 import BeautifulSoup
import requests
from collections import Counter

class SoupScraper:
    def __init__(self, url):
        self.url = url
        self.soup = []

    def scrape(self, num_pages):
        '''Returns beautiful soup object after scraping given URL location across x pages'''
        for page in range(1, num_pages + 1):
            resp = requests.get(self.url + 'page/' + str(page))
            print(f"Scraping page {page}...")
            soup_page = BeautifulSoup(resp.text, 'html.parser')
            self.soup.append(soup_page)

    def get_tags(self):
        '''Returns a list of all href tag instances in the scraped page'''
        tags = [[tag.contents[0] for tag in page.find_all('a')] for page in self.soup]
        flat_list = [item for sublist in tags for item in sublist]
        return flat_list

    def most_frequent(self, tags):
        '''Returns dict of the 10 most frequently occuring tags and their frequencies'''
        most_common = Counter(tags).most_common(10)
        return {k:v for (k,v) in most_common}

if __name__ == '__main__':
    scraper = SoupScraper('http://quotes.toscrape.com/')
    scraper.scrape(10)
    #print(scraper.soup)
    tags_list = scraper.get_tags()
    #print(tags_list)
    most_frequent = scraper.most_frequent(tags_list)
    print(most_frequent)