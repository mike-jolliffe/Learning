def pprint_phone(phone_string):
  '''Given an all digit input, returns a formatted phone number'''
  print("({}) {}-{}".format(phone_string[:3], phone_string[3:6], phone_string[6:]))

phone_string = input("Give me your phone number: ")
pprint_phone(phone_string)
