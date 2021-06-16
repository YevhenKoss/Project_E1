from collections import UserDict


class Assistant(UserDict):

    def add_record(self, record):
        contact_number = len(self.data) + 1
        self.data[contact_number] = record
        contact_number += 1
        return contact_number


class Name():

    def __init__(self, name):
        self.name = name.capitalize()


class Phone():

    def __init__(self, phone):
        self.phone = phone


class Email():

	def __init__(self, email):
		self.email = email


class Address():

	def __init__(self, address):
		self.address = address


class Record():

    def __init__(self, name, phone, email, address, birthday):
        phones = []
        phones.append(phone.phone)
        self.contact_data = contact_data = {}
        self.name = contact_data['Name'] = name.name
        self.phone = contact_data['Phone'] = phones
        self.email = contact_data['Email'] = email
        self.email = contact_data['Address'] = address
        if birthday != None and birthday != '':
            self.birthday = contact_data['Birthday'] = birthday.birthday
        else:
            self.birthday = None