'''
* URL open the [main listing website](http://or.water.usgs.gov/non-usgs/bes/).
  1. Use BeautifulSoup to parse the main site making hyperlinks for all the rain table pages.
  2. Allow user to select from a list of current/available rain gages
  3. Given user's args, send requests for those gages via associated hyperlinks
  4. Ask for future date, if user wants a prediction
  5. Return a table of the following statistics by gage:
        * The specific date with the most rain.
        * The year with the most rain.
        * Find and print the day of the year with the most rain on average.
          E.g. December 30th has 1" of rain on average.
        * Predicted amount of rain for a given date







'''