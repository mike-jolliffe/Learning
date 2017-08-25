import json

class PhoneBook():
    '''Create a program that uses a dictionary to store phonebook
    entries. Must have user interaction.
    Include ability to:
    1. Search
    2. Add Entry
    3. Change Entry
    4. Delete Entry
    5. Exit Program
    '''

    def __init__(self, infile):
        try:
            # if a phonebook file already exists, open and decode the JSON object
            self.infile = infile
            with open(self.infile, 'w') as for_json:
                self.phonebook = json.load(for_json)
            print("opened existing file")
        except OSError:
            # if the phonebook file doesn't exist, initialize a new dictionary
            print ("couldn't open existing file")
            self.phonebook = {}

    def getStatus(self):
        return self.phonebook

    def search(self, searchword):
        '''Allow search functionality'''
        if searchword in self.phonebook:
            return f"{self.phonebook[searchword]}"

    def addEntry(self, namesplit, phone):
        '''Allow insertion of new entry into dict'''
        if not ''.join(namesplit) in self.phonebook:
            self.phonebook[''.join(namesplit)] = {'name': ' '.join(namesplit), 'phone': phone}
            return f"{namesplit[0]} {namesplit[1]} successfully added to phonebook."

    def changeEntry(self, name_key, new_phone):
        '''Allow change of existing entry in dict'''
        if name_key in self.phonebook:
            self.phonebook[name_key]['phone'] = new_phone
            return f"phone number successfully modified"

    def deleteEntry(self, searchword):
        '''Allow entry deletion'''
        if searchword in self.phonebook:
            del self.phonebook[searchword]
            return f"entry successfully deleted"

    def leaveProgram(self):
        '''Exit program'''
        json.dump(self.phonebook, self.infile)
        self.infile.close()
        exit()

    def run(self, keyword):

        self.keyword = keyword

        if self.keyword == 'status':
            print(self.getStatus())

        elif self.keyword in ['s', 'search', 'Search']:
            searchword = input("what would you like to search for? ")
            print(self.search(searchword.replace(" ", "")))

        elif self.keyword in ['a', 'add', 'Add']:
            name = input("Who would you like to add? ")
            namesplit = name.split()
            phone = input("What's their phone number? ")
            print(self.addEntry(namesplit, phone))

        elif self.keyword in ['c', 'change']:
            searchword = input("Whose phone number would you like to change? ")
            name_key = searchword.replace(" ", "")
            new_phone = input("What's the new phone number? ")
            print(self.changeEntry(name_key, new_phone))

        elif self.keyword in ['d', 'delete']:
            searchword = input("Who would you like to delete from the phonebook? ")
            print(self.deleteEntry(searchword.replace(" ", "")))

        elif self.keyword in ['e', 'exit', 'Exit', 'x']:
            self.leaveProgram()

        else:
            print (f"Input not recognized.")

if __name__ == '__main__':
    print()
    print()
    print()
    print(f"Welcome to the phonebook")
    Phone_Book = PhoneBook('phonebook.json')
    while True:
        print()
        print()
        print(f'''
        To get status: status. \n
        To search: s, search, or Search.\n
        To add: a, add, or Add. \n
        To change: c, or change. \n
        To delete: d, or delete.\n
        To exit: e, or exit.\n''')
        keyword = input("What action would you like to take? ")
        print()
        print()
        Phone_Book.run(keyword)
