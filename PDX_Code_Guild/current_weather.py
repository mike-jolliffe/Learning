import requests

class WeatherGetter(object):
    '''Will create an object that accesses the Open Weather Map api'''

    def __init__(self):
        self.units = ['metric', 'imperial']

    def get_weather(self, location, unit='1'):
        '''Given a location (either zip or city), sends a request to Open Weather Map API, returns a current weather JSON
        object'''

        package = {
            'APPID': '0a782a90c9c00349d94ab5ca05d3679c',
            'q': location,
            'zip': None,
            'units': self.units[int(unit)]
        }

        resp = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

        return resp.json()

    def display_weather(self, units, response):
        '''Displays current weather for a given location'''
        print(f"-------- CURRENT WEATHER FOR {location.upper()} --------")
        print()
        print()
        print(f"Temperature: {response['main']['temp']} degrees XX")
        print(f"Humidity: {response['main']['humidity']}%")
        print(f"Cloudiness: {response['clouds']['all']}%")
        try:
            print(f"Rain in past 3 hours: {response['rain']['3h']} XX")
        except:
            print(f"Rain in past 3 hours: 0 XX")
        print(f"Wind is {response['wind']['speed']} XXX from {response['wind']['deg']} degrees")
        exit()

if __name__ == '__main__':
    weather = WeatherGetter()
    location = input("For what city or zipcode would you like to see current weather? ")
    print(f'''1 -- Metric \n2 -- Imperial''')
    units = int(input("What units would you like? ")) - 1
    report = weather.get_weather(location, units)
    print()
    print(weather.display_weather(units, report))