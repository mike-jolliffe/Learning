class UnitsConverter(Object):
    '''This class is used to convert between various units'''

    # Create a dictionary of metric prefixes
    metprefix_dict = {'exa':10**18, 'peta':10*15, 'tera':10**12,
                  'giga':10**9, 'mega':10**6, 'kilo':10*3,
                  'hecto':10**2, 'deca':10**1, '':10**0,
                  'deci':10**-1, 'centi':10**-2, 'milli':10**-3,
                  'micro':10**-6, 'nano':10**-9, 'pico':10**-12,
                  'femto':10**-15, 'atto':10**-18}

    # Create volume to liters specific conversion dict
    vol_dict = {'gallons': 3.78541, 'liters': 1}

    # Create in/mi to meters distance conversion
    dist_dict = {'inches': 0.0254, 'miles':1609.34, 'meters':1}

    def __init__(self, value, input_units, output_units):
        '''Instantiate an object for converting given value from current to
        target units'''
        self.value = value
        self.input_units = input_units
        self.output_units = output_units

    # create a function that converts input value and units to value in base units
    def convert_to_base(self):
        '''Returns a conversion of distance or volume into base units'''
        pass

    # create a function that converts base unit to target units
    def base_to_target(self):
        '''Returns a conversion from base units into target units'''
        pass

    # create a function to screen user input and call conversion functions
    def run(self):
        # Check whether either of the units are in dist_dict or vol_dict
        pass
        #distance = {key:value for (key,value) in dist_dict.items if key in self.input_units}

    # TODO raise error if trying to jump from dist_dict to vol_dict or vice-versa
