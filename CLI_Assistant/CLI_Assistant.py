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


