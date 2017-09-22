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

class SoupParser:
    def __init__(self, SoupScraper):
        self.soup = SoupScraper.soup

    def get_contents_of_tag_type(self, tag):
        '''Returns a list of all contents in a given tag'''
        tags = [[tag.contents[0] for tag in page.find_all(tag)] for page in self.soup]
        flat_list = [item for sublist in tags for item in sublist]
        return flat_list

    def most_frequent_quote_types(self, tags):
        '''Returns dict of the 10 most frequently quote categories and their frequencies'''
        most_common = Counter(tags).most_common(10)
        return {k:v for (k,v) in most_common}

    def quotes_dict(self, tags):    #TODO finish this function
        '''Returns a dictionary of quotes by author'''
        pass

if __name__ == '__main__':
    scraper = SoupScraper('http://quotes.toscrape.com/')
    scraper.scrape(10)
    #print(scraper.soup)
    parser = SoupParser(scraper)

    # Get 10 most frequent quote categories and their frequencies
    tags_list = parser.get_contents_of_tag_type('a')
    most_frequent = parser.most_frequent_quote_types(tags_list)
    print(most_frequent)

    # TODO Get all quotes by author