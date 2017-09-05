class Item(object):
    '''Used to create an item, describe it, and make it do things'''
    def __init__(self, description, location, damage):
        self.description = description
        self.location = location
        self.damage = damage
