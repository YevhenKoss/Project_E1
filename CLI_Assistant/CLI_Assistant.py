import CLI_Assistant_Classes
import pathlib
import pickle
import re


def add_function(command, bot_memory):
	if command == 'add':
		name = input("Enter abonent's name: ")
		name = CLI_Assistant_Classes.Name(name)
		phone = input(f"Enter {name.name}'s phone in format +XX(XXX)XXX-XX-XX: ")
		phone = CLI_Assistant_Classes.Phone(phone)
		email = input(f"Enter {name.name}'s email: ")
		if email:
			email = CLI_Assistant_Classes.Email(email)
		else:
			email = None
		address = input(f"Enter {name.name}'s address: ")
		if address:
			address = CLI_Assistant_Classes.Address(address)
		else:
			address = None
		birthday = input(f"Enter {name.name}'s birthday in format DD.MM.YYYY: ")
		if birthday:
			birthday = CLI_Assistant_Classes.Birthday(birthday)
		else:
			birthday = None

		record = CLI_Assistant_Classes.Record(name, phone, email, address, birthday)
		bot_memory.add_record(record)

		print(f'Record {bot_memory.data[len(bot_memory.data)].contact_data} created!')
		return bot_memory

def append_function(command, bot_memory):
	if command == 'append':
		find_data = input("If you want to append abonent's phone, enter his/her name or existing phone number in format +XX(XXX)XXX-XX-XX: ")
		find_result = bot_memory.find(find_data)
		if find_result != []:
			for j in range(0, len(find_result)):
				print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}')
			number_of_contact = input("Enter the number of contact phone you want to append: ")
			if number_of_contact.isdigit():
				for j in range(0, len(find_result)):
					if int(number_of_contact) == find_result[j][0]:
						new_phone = input("Enter new phone number: ")
						bot_memory.data[int(number_of_contact)].add_phone(new_phone)
						print(f"New phone number appended to current contact. Existing record changed on {bot_memory.data[int(number_of_contact)].contact_data}")
		else:
			print('No such abonent in phone book')

def birthday_function(command, bot_memory):
	if command == 'days to birthday':
		find_data = input("If you want to know how many days to abonent's birthday (only for abonents with date of birth), enter his/her name or existing phone number in format +XX(XXX)XXX-XX-XX: ")
		find_result = bot_memory.find(find_data)
		if find_result != []:
			for j in range(0, len(find_result)):
				print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}')
			number_of_contact = input("Enter the number of contact you want to know how many days to his/her Birthday: ")
			if number_of_contact.isdigit():
				for j in range(0, len(find_result)):
					if int(number_of_contact) == find_result[j][0]:
						bot_memory.data[int(number_of_contact)].days_to_birthday()
		else:
			print('No such abonent in phone book')

def change_phone_function(command, bot_memory):
	if command == 'change phone':
		find_data = input("If you want to change abonent's phone, enter his/her name or phone number in format +XX(XXX)XXX-XX-XX: ")
		find_result = bot_memory.find(find_data)
		if find_result != []:
			for j in range(0, len(find_result)):
				print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}')
			number_of_contact = input("Enter the number of contact you want to change: ")
			if number_of_contact.isdigit():
				for j in range(0, len(find_result)):
					if int(number_of_contact) == find_result[j][0]:
						existing_phone = input("Enter existing phone number you want to change: ")
						new_phone = input("Enter new phone number: ")
						bot_memory.data[int(number_of_contact)].edit_phone(existing_phone, new_phone)
						print(f'Change completed. Existing record changed on {bot_memory.data[int(number_of_contact)].contact_data}')
					else:
						print('Wrong number of contact')
			else:
				print('Wrong number of contact')
		else:
			print('No such abonent in phone book')

def hello_function(command):
	if command == 'hello':
		print('Hello! How can I help you?')

def input_command(input_data):
	commands = ['hello', 'add', 'append', 'change phone', 'days to birthday', 'phone', 'remove', 'save', 'show all', 'good bye', 'close', 'exit', 'find']
	for command in commands:
		if re.findall(command, input_data, re.IGNORECASE):
			result = command
			break
		else:
			result = f'{input_data} is unknown. Please enter one of commands: {", ".join(commands)}'
	return result

def phone_function(command, bot_memory):
	if command == 'phone':
		find_data = input("Enter abonent's name you want to find: ")
		find_result = bot_memory.find(find_data)
		if find_result != []:
			for j in range(0, len(find_result)):
				print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}')
		else:
			print('No such abonent in phone book')

def remove_function(command, bot_memory):
	if command == 'remove':
		find_data = input("If you want to remove abonent's phone, enter his/her name or existing phone number in format +XX(XXX)XXX-XX-XX: ")
		find_result = bot_memory.find(find_data)
		if find_result != []:
			for j in range(0, len(find_result)):
				print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}')
			number_of_contact = input("Enter the number of contact phone you want to remove: ")
			if number_of_contact.isdigit():
				for j in range(0, len(find_result)):
					if int(number_of_contact) == find_result[j][0]:
						removing_phone = input("Enter phone number you want to remove: ")
						for i in bot_memory.data[int(number_of_contact)].contact_data['Phone']:
							if i == removing_phone: 
								bot_memory.data[int(number_of_contact)].remove_phone(removing_phone)
								res = f"Chousen phone number is removed. Existing record changed on {bot_memory.data[int(number_of_contact)].contact_data}"
							else:
								res = 'No such phone in this contact'
						print(res)
		else:
			print('No such abonent in phone book')

def save_function(command, bot_memory):
	if command == 'save':
		with open('save.bin', 'wb') as file:
			pickle.dump(bot_memory, file)
			print('Data saved')
			
def show_all_function(command, bot_memory):
	if command == 'show all':
		for i in bot_memory:
			print(i)



def find_function(command, bot_memory):
	if command == 'find':
		find_data = input("To find abonent, enter his/her name or phone number in format +XX(XXX)XXX-XX-XX: ")
		find_result = bot_memory.find(find_data)
		if find_result != []:
			for j in range(0, len(find_result)):
				if len(find_result[j]) == 3:
					print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}')
				elif len(find_result[j]) == 4:
					print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}, Email: {find_result[j][3]}')
				elif len(find_result[j]) == 5:
					print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}, Email: {find_result[j][3]}, Address: {find_result[j][4]}')
				elif len(find_result[j]) == 6:
					print(f'Contact № {find_result[j][0]}, Name: {find_result[j][1]}, Phone: {find_result[j][2]}, Email: {find_result[j][3]}, Address: {find_result[j][4]}, Birthday: {find_result[j][5]}')


	





	
















