class UnitsConverter():
    '''This class is used to convert between various units'''

    # Create a dictionary of metric prefixes
    metprefix_dict = {'exa':10**18, 'peta':10*15, 'tera':10**12,
                  'giga':10**9, 'mega':10**6, 'kilo':10*3,
                  'hecto':10**2, 'deca':10**1, 'deci':10**-1, 'centi':10**-2,
                  'milli':10**-3, 'micro':10**-6, 'nano':10**-9, 'pico':10**-12,
                  'femto':10**-15, 'atto':10**-18}

    # Create volume to liters specific conversion dict
    vol_dict = {'gallons': 3.78541, 'liters': 1}

    # Create in/mi to meters distance conversion
    dist_dict = {'inches': 0.0254, 'miles':1609.34, 'meters':1}

    def __init__(self, value, input_units, output_units):
        '''Instantiate an object for converting given value from current to
        target units'''
        self.value = int(value)
        self.input_units = input_units
        self.output_units = output_units

    # create a function that converts input value and units to value in base units
    def convert_to_base(self):
        '''Returns a conversion of distance or volume into base units'''
        converter = self.input_check()
        print("Converter: {}".format(converter))
        # Get the base value in meters or liters
        base = self.value * converter[0]
        # Modify the base value according to prefix in metprefix dictionary
        prefix_mod_in = [value for (key,value) in self.metprefix_dict.items() if key in self.input_units]

        # If the user input units have any prefixes in front of meters/liters
        if prefix_mod_in:
            # Modify the base value accordingly
            return base * prefix_mod_in[0]
        else:
            # Otherwise, just return the base value
            return base

    # create a function that converts base unit to target units
    def base_to_target(self):
        '''Returns a conversion from base units into target units'''
        # Check for prefix mod on output_units
        prefix_mod_out = [value for (key,value) in self.metprefix_dict.items() if key in self.output_units]
        base_value = self.convert_to_base()
        if prefix_mod_out:
            target_val = prefix_mod_out[0] * base_value
        else:
            target_val = base_value
        print("{} {} converts to {} {}.".format(self.value, self.input_units, target_val, self.output_units))

    # create a function to screen user input and call conversion functions
    def input_check(self):
        # Check whether either of the units are in dist_dict or vol_dict
        distance_in = {key:value for (key,value) in self.dist_dict.items() if key in self.input_units}
        distance_out = {key:value for (key,value) in self.dist_dict.items() if key in self.output_units}
        volume_in = {key:value for (key,value) in self.vol_dict.items() if key in self.input_units}
        volume_out = {key:value for (key,value) in self.vol_dict.items() if key in self.output_units}

        # make sure user isn't trying to convert volume to dist, or vice versa
        if not len(distance_in) == len(distance_out) and not len(volume_in) == len(volume_out):
            raise ValueError("Cannot convert between distances and volumes.")
        # grab the value required for conversion
        if len(distance_in) > 0:
            # meters for that unit
            return [values for values in distance_in.values()]
        elif len(volume_in) > 0:
            # liters for that unit
            return [values for values in volume_in.values()]
        else:
            print("Invalid distance/volume units.")




if __name__ == "__main__":
    value = input("Enter a magnitude: ")
    input_units = input("Enter current units: ")
    output_units = input("Enter desired units: ")
    new_conv = UnitsConverter(value, input_units, output_units)
    new_conv.base_to_target()
