'''
* URL open the [main listing website](http://or.water.usgs.gov/non-usgs/bes/).
  2. Allow user to select from a list of current/available rain gages
  3. Given user's args, send requests for those gages via associated hyperlinks
  4. Ask for future date, if user wants a prediction'''


from bs4 import BeautifulSoup
from datetime import datetime
import requests


class RainReport():
    '''Creates an object that scrapes rain gage data, returns descriptive stats about rainfall at various
    locations in Oregon'''

    def __init__(self):
        self.base_url = "http://or.water.usgs.gov/non-usgs/bes/"
        self.table_data = ""
        # Dictionary to hold all scraped/parsed gage data desired by user
        self.gage_dictionary = {}
        # Menu-style dictionary to hold an int key and [gage location, gage url snippet], from which user can select
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
                self.gage_locations[gage_index] = [gage[0]]
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
        '''Creates/updates dictionary of gage locations and associated observations. Returns location key for use
        by other functions'''
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
        obs_values = [[int(val) if val.isdigit() else -0.0001 for val in day] for day in obs_values]
        #check=[(print('-' in day)) for day in obs_values]


        # Zip those total and hourly obervations into a dictionary
        daily_obs = [dict(zip(obs_keys, day)) for day in obs_values]
        # zip each daily observation pair as a value into its own date dictionary
        date_obs = dict(zip(date_keys, daily_obs))

        # Get gage location for the table and link all date keys as values into that location
        location_key = days[0]
        location_dict[location_key] = date_obs
        self.gage_dictionary.update(location_dict)
        return location_key

    def get_rainiest(self, location_key, *date_args):
        '''Return stats for rainiest year, day, amount for given day in history of that gaging station'''
        # Create dictionary of date, precip totals for given location key
        x = {x: self.gage_dictionary[location_key][x]['Total'] for x, y in self.gage_dictionary[location_key].items()}

        # Return the highest observed rain value across all days at the given location
        highest_abs_daily = [(k, v) for k, v in x.items() if v == max(x.values())][0]

        # Create dictionary to store observations by year
        year_rain = {}
        for year in x:
            if not year[0] in year_rain:
                year_rain[year[0]] = x[year]
            else:
                year_rain[year[0]] += x[year]

        # Grab the year with the highest total rain amount
        highest_rain_year = [(k,v) for k, v in year_rain.items() if v == max(year_rain.values())]

        # Create dictionary to store observations by day
        obs_by_day = {}
        for day in x:
            if not (day[1], day[2]) in obs_by_day:
                obs_by_day[(day[1], day[2])] = [x[day]]
            else:
                obs_by_day[(day[1], day[2])].append(x[day])

        # Create dictionary of average rainfall for each day of a year
        daily_avg = {}
        for day in obs_by_day:
            daily_avg[day] = sum(obs_by_day[day])/len(obs_by_day[day])

        # If user provides a date for grabbing stats
        if date_args:
            # Grab the average, max, and minimum rainfall for that day of the year
            avg_date = daily_avg[date_args]
            max_date = max([v for v in obs_by_day[date_args]])
            min_date = min([v for v in obs_by_day[date_args]])
            date_stats = [max_date, min_date, avg_date]
        # Otherwise, grab the max and day of year for max, min and day of year for min
        else:
            max_day_absolute = [(k,v) for k, v in daily_avg.items() if v == max(daily_avg.values())]
            min_day_absolute = [(k,v) for k, v in daily_avg.items() if v == min(daily_avg.values())]
            date_stats = [max_day_absolute, min_day_absolute]

        return (highest_abs_daily, highest_rain_year, date_stats)

if __name__ == '__main__':
    report = RainReport()
    # Scrape the gage homepage to get hrefs for tables of all gage locations
    soup = report.scrape_home()
    report.get_gage_locs(soup)
    hrefs = report.get_table_locs(soup)
    # Print available gage locations for user to choose from
    for location in report.gage_locations:
        report.gage_locations[location].append(hrefs[location-1])
        print (f"{location} -- {report.gage_locations[location][0]}")
    location_input = int(input("Please pick a location: "))
    table_to_scrape = report.gage_locations[location_input]
    report.get_table(table_to_scrape[1])
    # Parse the location data into a dictionary
    location = report.parse_to_dict()
    # Grab a date of interest from a user, if they have one
    date_of_interest = tuple(input("Enter month day for date statistics, or 0 for general stats: ").split())
    # If user provides a particular date of interest
    if not int(date_of_interest[0]) == 0:
        # Grab and print the max, min, avg precipitation for that date
        highest_day, highest_year, date_stats = report.get_rainiest(location, int(date_of_interest[0]), int(date_of_interest[1]))
        print()
        print(f"Precipitation at {table_to_scrape[0]} for {date_of_interest[0]}/{date_of_interest[1]}\n"
              f"Predicted: {date_stats[2]/100:.2f}\n"
              f"max: {date_stats[0]/100: .2f}\n"
              f"min: {date_stats[1]/100:.2f}")
    # If user doesn't provide particular date of interest
    else:
        # Grab and print date and amounts of max average precip, min avg precip
        highest_day, highest_year, date_stats = report.get_rainiest(location)
        print()
        print(f"----- RAIN STATS FOR {table_to_scrape[0].upper()} -----")
        print()
        print(f"{date_stats[0][0][0][0]}/{date_stats[0][0][0][1]} the rainiest day on average with {date_stats[0][0][1]/100:.2f} " \
              f"inches of precipitation.\n \n" \
              f"{date_stats[1][0][0][0]}/{date_stats[1][0][0][1]} is the least rainy day on average with {abs(date_stats[1][0][1]/100):.2f} " \
              f"inches of precipitation.")
    print()
    print(f"The rainiest day ever recorded was {highest_day[0][1]}/{highest_day[0][2]}/{highest_day[0][0]}" \
          f" with {highest_day[1]/100:.2f} inches of precipitation.")
    print()
    print(f"The rainiest year ever recorded was {highest_year[0][0]} with {highest_year[0][1]/100:.2f} inches of precipitation.\n")

