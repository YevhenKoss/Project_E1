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

    def add_phone(self, phone):
        if phone.isdigit() and len(phone) == 12:
            self.contact_data['Phone'].append(phone)
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            self.phone = None

    def edit_phone(self, phone, new_phone):
        if phone.isdigit() and len(phone) == 12:
            phone = phone
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            phone = None
        if new_phone.isdigit() and len(new_phone) == 12:
            new_phone = new_phone
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            new_phone = phone
        for i in self.contact_data['Phone']:
            if i == phone:
                idx = self.contact_data['Phone'].index(i)
                self.contact_data['Phone'][idx] = new_phone

    def remove_phone(self, phone):
        if phone.isdigit() and len(phone) == 12:
            self.contact_data['Phone'].remove(phone)
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')

    def days_to_birthday(self):
        if self.birthday != None:
            today = date.today()
            dob_data = self.birthday.split(".")
            dobDay = int(dob_data[0])
            dobMonth = int(dob_data[1])
            dobYear = int(dob_data[2])
            dob = date(dobYear,dobMonth,dobDay)
            thisYear = today.year
            nextBirthday = date(thisYear,dobMonth,dobDay)
            if today < nextBirthday:
                gap = (nextBirthday - today).days
                print("Abonent's birhday is in " + str(gap) + ' days.')
            elif  today == nextBirthday:
                print("Today is abonent's birthday! Happy Birthday!")
            else:
                nextBirthday = date(thisYear+1,dobMonth,dobDay)
                gap = (nextBirthday - today).days
                print("Abonent's birthday is in " + str(gap) + ' days.')
        else:
            print("Current contact doesn't have date of birth")