'''
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

    def get_contents_of_tag_type(self, tag, start=0, stop=None):
        '''Returns a list of all contents in a given tag'''
        tags = [[tag.contents[start:stop] for tag in page.select(tag)] for page in self.soup]
        flat_list = [item for sublist in tags for item in sublist]
        return flat_list

    def most_frequent_quote_types(self, tags):
        '''Returns dict of the 10 most frequently quote categories and their frequencies'''
        tags = [tag[0] for tag in tags]  # Indexing to eliminate single-element lists
        most_common = Counter(tags).most_common(10)
        return {k:v for (k,v) in most_common}  # Indexing to eliminate single element lists again

    def quotes_dict(self, quotes, authors):
        '''Returns a dictionary of quotes by author'''
        # Zip author/quote lists together as list of tuples
        zipped = []
        for i, j in zip(authors, quotes):
            zipped.append((i[0],j[0])) # Just indexing to eliminate single-element list issue

        quotes_dict = {}
        for author_quotes in zipped:
            # new approach, much tighter than "if not key in dict, add key-value, else append value to key"
            quotes_dict.setdefault(author_quotes[0], []).append(author_quotes[1])
        return quotes_dict

if __name__ == '__main__':
    scraper = SoupScraper('http://quotes.toscrape.com/')
    scraper.scrape(10)
    parser = SoupParser(scraper)
    #print(parser.soup)
    #Get 10 most frequent quote categories and their frequencies
    tags_list = parser.get_contents_of_tag_type('a', 0, 1)
    #print(tags_list)
    most_frequent = parser.most_frequent_quote_types(tags_list)
    print(f"Most frequent quote types: {most_frequent}\n")


    quotes = parser.get_contents_of_tag_type("div .text", stop=1)
    authors = parser.get_contents_of_tag_type("small", stop=1)
    print(parser.quotes_dict(quotes, authors))