from collections import UserDict
from datetime import date
import re



class Assistant(UserDict):

    def add_record(self, record):
        contact_number = len(self.data) + 1
        self.data[contact_number] = record
        contact_number += 1
        return contact_number

    def find(self, find_data):
        result = []
        for k, i in self.data.items():
            if len(i.contact_data) == 2:
                if re.findall(find_data, i.contact_data['Name'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone']])
                else:
                    for j in range(0, len(i.contact_data['Phone'])):
                        if re.findall(find_data, i.contact_data['Phone'][j], re.IGNORECASE) != []:
                            result.append([k, i.contact_data['Name'], i.contact_data['Phone']])
            elif len(i.contact_data) == 3:
                if re.findall(find_data, i.contact_data['Name'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email']])
                elif re.findall(find_data, i.contact_data['Email'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email']])
                else:
                    for j in range(0, len(i.contact_data['Phone'])):
                        if re.findall(find_data, i.contact_data['Phone'][j], re.IGNORECASE) != []:
                            result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email']])
            elif len(i.contact_data) == 4:
                if re.findall(find_data, i.contact_data['Name'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address']])
                elif re.findall(find_data, i.contact_data['Email'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address']])
                elif re.findall(find_data, i.contact_data['Address'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address']])
                else:
                    for j in range(0, len(i.contact_data['Phone'])):
                        if re.findall(find_data, i.contact_data['Phone'][j], re.IGNORECASE) != []:
                            result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address']])
            elif len(i.contact_data) == 5:
                if re.findall(find_data, i.contact_data['Name'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address'], i.contact_data['Birthday']])
                elif re.findall(find_data, i.contact_data['Email'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address'], i.contact_data['Birthday']])
                elif re.findall(find_data, i.contact_data['Address'], re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address'], i.contact_data['Birthday']])
                elif re.findall(find_data, str(i.contact_data['Birthday']), re.IGNORECASE) != []:
                    result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address'], i.contact_data['Birthday']])
                else:
                    for j in range(0, len(i.contact_data['Phone'])):
                        if re.findall(find_data, i.contact_data['Phone'][j], re.IGNORECASE) != []:
                            result.append([k, i.contact_data['Name'], i.contact_data['Phone'], i.contact_data['Email'], i.contact_data['Address'], i.contact_data['Birthday']])
        return result



    def __getstate__(self):
        attributes = self.__dict__
        return attributes
    
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        keys = tuple(self.data.keys())
        if self.index == len(keys):
            raise StopIteration
        key = keys[self.index]
        record = self.data[key]
        self.index += 1
        return record.name, record.phone, record.email, record.address, record.birthday


class Name():

    def __init__(self, name):
        self.__name = name.capitalize()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()




class Phone():

    def __init__(self, phone):
        self.__phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone



class Email():

    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def phone(self, email):
        self.__email = email



class Address():

	def __init__(self, address):
		self.address = address


class Birthday():

    def __init__(self, birthday):
        if birthday != 'empty birthday date':
            birthday = str(birthday)
            dob_data = birthday.split(".")
            today = date.today().year
            if dob_data[0].isdigit and int(dob_data[0]) > 0 and int(dob_data[0]) <= 31:
                if dob_data[1].isdigit and int(dob_data[1]) > 0 and int(dob_data[1]) <= 12:
                    if dob_data[2].isdigit and int(dob_data[2]) > 0 and int(dob_data[2]) <= today:
                        res = birthday
                    else:
                        print('You enter wrong year')
                        res = None
                else:
                    print('You enter wrong month')
                    res = None
            else:
                print('You enter wrong day')
                res = None
        else:
            res = 'empty birthday date'
        self.birthday = res


class Record():

    def __init__(self, name, phone, email, address, birthday):
        phones = []
        phones.append(phone.phone)
        self.contact_data = contact_data = {}
        self.name = contact_data['Name'] = name.name
        self.phone = contact_data['Phone'] = phones
        self.email = contact_data['Email'] = email.email
        self.address = contact_data['Address'] = address.address
        self.birthday = contact_data['Birthday'] = birthday.birthday

    def add_phone(self, phone):
        self.contact_data['Phone'].append(phone)

    def edit_phone(self, phone, new_phone):
        for i in self.contact_data['Phone']:
            if i == phone:
                idx = self.contact_data['Phone'].index(i)
                self.contact_data['Phone'][idx] = new_phone

    def edit_email(self, new_email):
        self.contact_data['Email'] = new_email




    def remove_phone(self, phone):
        self.contact_data['Phone'].remove(phone)


    def days_to_birthday(self):
        if self.birthday != 'empty birthday date':
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
