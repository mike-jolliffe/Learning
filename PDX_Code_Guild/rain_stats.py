'''
* URL open the [main listing website](http://or.water.usgs.gov/non-usgs/bes/).
  2. Allow user to select from a list of current/available rain gages
  3. Given user's args, send requests for those gages via associated hyperlinks
  4. Ask for future date, if user wants a prediction
  5. Return a table of the following statistics by gage:
        * The specific date with the most rain.
        * The year with the most rain.
        * Find and print the day of the year with the most rain on average.
          E.g. December 30th has 1" of rain on average.
        * Predicted amount of rain for a given date'''

from bs4 import BeautifulSoup
from datetime import datetime
import requests


class RainReport():
    '''Creates an object that scrapes rain gage data, returns descriptive stats about rainfall at various
    locations in Oregon'''

    def __init__(self):
        self.base_url = "http://or.water.usgs.gov/non-usgs/bes/"
        self.table_data = ""
        self.gage_dictionary = {}
        self.gage_locations = {}

    def scrape_home(self):
        '''Scrapes html from the base url location'''
        resp = requests.get(self.base_url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup

    def get_gage_locs(self, soup):
        '''Returns a dictionary of all gage locations with an integer as key'''
        gage_index = 1
        gage_tags = soup.find_all('td')
        gages = [gage.contents for gage in gage_tags]
        for gage in gages:
            if not soup.strong in gage and soup.br in gage:
                self.gage_locations[gage_index] = gage[0]
                gage_index += 1
        return self.gage_locations

    def get_table_locs(self, soup):
        '''Parses a base_url for all anchor tags to rain gage tables. Returns those url snippets.'''
        hrefs = [anchor['href'] for anchor in soup.find_all('a', href=True) if ".rain" in anchor['href']]
        return hrefs

    def get_table(self, href):
        '''Returns a single text table of rain data associated with a given gage'''
        table_data = requests.get(self.base_url+href)
        self.table_data = table_data.text
        return self.table_data

    def parse_to_dict(self):
        # Initialize a location dictionary
        location_dict = {}
        # Grab the raw table data that was scraped
        days = self.table_data.splitlines()

        # Convert years, months, days strings into tuples for later statistical use
        date_keys = [elmnt.split()[0] for elmnt in days[11:]]
        date_keys = [datetime.strptime(elmnt, '%d-%b-%Y').date() for elmnt in date_keys]
        date_keys = [(date.year, date.month, date.day) for date in date_keys]

        # Grab total and hourly precip observations for a given day
        obs_keys = days[9].split()[1:]
        obs_values = [elmnt.split()[1:] for elmnt in days[11:]]
        obs_values = [[int(val) if val.isdigit() else val for val in day] for day in obs_values]
        #check=[(print('-' in day)) for day in obs_values]


        # Zip those total and hourly obervations into a dictionary
        daily_obs = [dict(zip(obs_keys, day)) for day in obs_values]
        # zip each daily observation pair as a value into its own date dictionary
        date_obs = dict(zip(date_keys, daily_obs))

        # Get gage location for the table and link all date keys as values into that location
        location_key = days[0]
        location_dict[location_key] = date_obs

        print(location_dict)

if __name__ == '__main__':
    report = RainReport()
    soup = report.scrape_home()
    report.get_gage_locs(soup)
    hrefs = report.get_table_locs(soup)
    report.get_table('astor.rain')
    report.parse_to_dict()

