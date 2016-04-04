"""
Project: Business Contacts
File: Main .py file
Name: Marshall Schmutz
Date: 4/01/2016
Description: A program to save business contacts
"""
import sys
import time

# The BusinessContacts class to create new contacts
class BusinessContacts():

	"""
	Method: __init__
	Purpose: Initialize the BusinessContacts class
	Parameters: self			-The parent class
				firstName		-First name of contact
				lastName		-Last name of contact
				phoneNumber 	-Phone number of contact
				emailAddress 	-Email address of contact
				company			-Company contact works for
	Returns: This method does not return a value
	"""
	def __init__(self, firstName, lastName, phoneNumber, emailAddress, company):
		self.firstName = firstName
		self.lastName = lastName
		self.fullName = firstName + ' ' + lastName
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress
		self.company = company

# The Main class.  Most everything is controlled here
class Main():

	"""
	Method: __init__
	Purpose: Initialize the Main class
	Parameters: self			-The parent class
	Returns: This method does not return a value
	"""
	def __init__(self):
		self.contactNames = []
		self.contactNumbers = []
		self.contactEmails = []
		self.contactCompanies = []

	"""
	Method: addContactToArrays
	Purpose: Add the newly created contact to the arrays
	Parameters:	self			-The parent class
				fullName		-new contact full name
				phoneNumber 	-new contact phone number
				emailAddress 	-new contact email address
				company 		-new contact company 
	Returns: This method does not return a value
	"""
	def addContactToArrays(self, fullName, phoneNumber, emailAddress, company):
		self.contactNames.append(fullName)
		self.contactNumbers.append(phoneNumber)
		self.contactEmails.append(emailAddress)
		self.contactCompanies.append(company)

	"""
	Method: addContactToFile
	Purpose: Add the newly created contact to the contacts.dat file
	Parameters:	self			-The parent class
				fullName		-new contact full name
				phoneNumber 	-new contact phone number
				emailAddress 	-new contact email address
				company 		-new contact company
	Returns: This method does not return a value
	"""
	def addContactToFile(self, fullName, phoneNumber, emailAddress, company):
		contactFile = open("contacts.dat", "a+")

		# Dump all new variables into one line
		# The organization should look like this:
		# Ryan Merrill,12345667,rmerrill@dxatc.edu,DXATC/John Smith,7654321,john@smith.com,Smith's
		contactFile.write(fullName + ',')
		contactFile.write(phoneNumber + ',')
		contactFile.write(emailAddress + ',')
		contactFile.write(company + '/')

		contactFile.close()

	"""
	Method: newContact
	Purpose: Create a new contact
	Parameters:	self			-The parent class
	Returns: This method does not return a value
	"""
	def newContact(self):
		# Gather info
		firstName = raw_input("First name: ")
		lastName = raw_input("Last name: ")
		phoneNumber = raw_input("Phone number: ")
		emailAddress = raw_input("Email address: ")
		company = raw_input("Company: ")

		# Add contact to arrays and file
		newContact = BusinessContacts(firstName, lastName, phoneNumber, emailAddress, company)
		self.addContactToArrays(newContact.fullName, newContact.phoneNumber, newContact.emailAddress, newContact.company)
		self.addContactToFile(newContact.fullName, newContact.phoneNumber, newContact.emailAddress, newContact.company)


	"""
	Method: cleanArrays
	Purpose: clean the arrays by emptying them and reloading the file into them
	Parameters:	self			-The parent class
	Returns: This method does not return a value
	"""
	def cleanArrays(self):
		self.contactNames[:] = []
		self.contactNumbers[:] = []
		self.contactEmails[:] = []
		self.contactCompanies[:] = []
		# print contactNames, contactNumbers, contactEmails, contactCompanies
		self.fileToArray()


	"""
	Method: deleteContact
	Purpose: Delete a selected contact
	Parameters:	self			-The parent class
	Returns: This method does not return a value
	"""
	def deleteContact(self):
		desiredContact = raw_input("What contact do you wish to delete? ")
		contactIndex = self.contactNames.index(desiredContact)

		# Remove contact data from file
		f = open("contacts.dat", "rw")
		data = f.readlines()
		if self.contactNames[contactIndex] in data:
			data.replace(self.contactNames[contactIndex], "")
		if self.contactNumbers[contactIndex] in data:
			data.replace(self.contactNumbers, "")
		if self.contactEmails[contactIndex] in data:
			data.replace(self.contactEmails, "")
		if self.contactCompanies[contactIndex] in data:
			data.replace(self.contactCompanies, "")
		f.close()

		# Remove contact data from arrays
		self.contactNames.pop(contactIndex)
		self.contactNumbers.pop(contactIndex)
		self.contactEmails.pop(contactIndex)
		self.contactCompanies.pop(contactIndex)

		print "The contact has been deleted"
		time.sleep(2)

	"""
	Method: viewContact
	Purpose: View a specific contact
	Parameters:	self			-The parent class
	Returns: This method does not return a value
	"""
	def viewContact(self):
		self.cleanArrays()
		desiredContact = raw_input("What contact would you like to view? ")
		contactIndex = self.contactNames.index(desiredContact)
		print ''
		print "Name: %s" % self.contactNames[contactIndex]
		print "Phone Number: %s" % self.contactNumbers[contactIndex]
		print "Email: %s" % self.contactEmails[contactIndex]
		print "Company: %s" % self.contactCompanies[contactIndex]
		time.sleep(2)

	"""
	Method: listContacts
	Purpose: list all contacts
	Parameters:	self			-The parent class
	Returns: This method does not return a value
	"""
	def listContacts(self):
		self.cleanArrays()
		for name in self.contactNames:
			print name
		time.sleep(2)

	"""
	Method: getContacts
	Purpose: get all the contacts from the file
	Parameters:	self			-The parent class
	Returns: This method returns a list of items from the file
	"""
	def getContacts(self):
		f = open("contacts.dat", "rb")
		contacts = f.read().split('/')
		contactBundle = []
		individualContact = []
		for contact in contacts:
			contactBundle.append(contact)
		x = 0
		for i in contactBundle:
			splits = i.split(',')
			for i in splits:
				if x == 0:
					i += "name"
				elif x == 1:
					i += "phone"
				elif x == 2:
					i += "email"
				elif x == 3:
					i += "company"
				else:
					x = 0
				individualContact.append(i)
				x += 1
		return individualContact
		f.close()

	"""
	Method: fileToArray
	Purpose: Convert data from file and store it in the arrays
	Parameters:	self			-The parent class
	Returns: This method does not return a value
	"""
	def fileToArray(self):
		for i in self.getContacts():
			if "name" in i:
				newI = i.replace("name", "")
				self.contactNames.append(newI)
			elif "phone" in i:
				newI = i.replace("phone", "")
				self.contactNumbers.append(newI)
			elif "email" in i:
				newI = i.replace("email", "")
				self.contactEmails.append(newI)
			elif "company" in i:
				newI = i.replace("company", "")
				self.contactCompanies.append(newI)
			else:
				self.contactNames.append(i)


	"""
	Method: action
	Purpose: Control flow and user input
	Parameters: self	-The parent class
	Returns: This method does not return a value
	"""
	def action(self):
		print "Business Contacts"
		print "1. Add a contact"
		print "2. Delete a contact"
		print "3. View information concerning a specific contact"
		print "4. Display contact list"
		print "99. Exit"
		userChoice = raw_input("What would you like to do? ")

		choices = {
		"1": self.newContact,
		"2": self.deleteContact,
		"3": self.viewContact,
		"4": self.listContacts,
		"99": sys.exit,
		}

		if userChoice not in choices:
			print "I'm sorry, that is not a valid option"
			print ''
			time.sleep(2)
		else:
			choices[userChoice.lower()]()
			print ''


# Main loop of program
main = Main()
while True:
	main.action()
