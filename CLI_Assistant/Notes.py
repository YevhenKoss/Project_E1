from collections import UserList


class Notes(UserList):

	def __init__(self, tag, note):
		super().__init__()
		self.tag = tag
		self.note = note
		record = {tag: note}
		self.data.append(record)


tag = '1'
note = 'first note'
note1 = Notes(tag, note)

print(note1.data)
