import random
import pandas as pd
#StudentDict = {}
StudentDict2 = {'ID':[],
				'Name':[],
				'Age':[],
				'Major':[],
				'Gender':[]}
#creates the student class
class Student(object):
	def __init__(self,name,age,major,gender):
		self.name = name
		self.age = age
		self.major = major
		self.gender = gender
	def studentinfo(self):
			return ("{name} is {age} years old and is majoring in {major}".format(name = self.name, age = self.age, major = self.major))

def studentinfo(studentid,name,age,major):
	return ("Student {studentid} is {name} is {age} years old and is majoring in {major}".format(studentid = studentid, name = name, age = age, major = major))


#prints instructions for the user
print ("\nWelcome to San Diego State Student Portal!\nHere you can enter student information.\n")

#While true statement to catch if a user isn't entering an integer value. Infinite loop until break. Will also identify the number of entries
def Num_entries():
	while True:
		try:
			number_of_entries = int(input("How many students are you entering: "))
			break
		except:
			print ("\nThat was not a valid number. Try again.\n")
	return number_of_entries
#Creating a for loop based on the number of entries user created. Count + 1 used since its based on an index
def entries ():
	for count in range(Num_entries()):
		inputname = input("\nWhat is the name of student #%s: " %(count+1))
		while True:
			try:
				inputage = int(input("What is their age: "))
				break
			except:
				print ("Please enter a number\n")
		inputmajor = input("What is their major: ")
		#User inputs gender, doing while loop to ensure that either male or female is entered. 
		while True:
			gender = input("Please enter a gender: ")
			if gender.lower() != "male" and gender.lower() != "female":
				print ("Please enter either male of female")
			else:
				break
		if gender.lower() == "male":
			himorher = "his"
		elif gender.lower() == "female":
			himorher = "her"
		#Student ID is generated randomly between ranges 1000-9999
		studentid = "SD%d" %(random.randrange(1000,9999))
		#Will determine if student ID generated already exists, prevents from duplicates 
		while True:
			if (studentid) in StudentDict2['ID']:
				(studentid) = "SD%d" %(random.randrange(1000,9999))
			else:
				break
		StudentDict2['ID'].append(studentid)
		StudentDict2['Name'].append(inputname)
		StudentDict2['Major'].append(inputmajor)
		StudentDict2['Age'].append (inputage)
		StudentDict2['Gender'].append(gender)
		##StudentDict[(studentid)] = ""
		print ("\n%s has been entered.\nThis is %s student id: %s\n" %(inputname.title(),himorher,studentid))
entries()
#i = 0
#for key in StudentDict:
	#StudentDict2[key] = Student(StudentDict2['Name'][i],StudentDict2['Age'][i],StudentDict2['Major'][i],StudentDict2['Gender'][i])
	#i+=1

#Prompts user to pull student data based on ID. 
while True:
	command = input("What would you like to do next?\n\nReport - Displays All Students\nInfo - Provides information about a student\nExit - Leave the Application\nAdd - Add additional students\n\n")
	if command.lower() == "exit":
		print ("\nGoodbye!\n")
		break
	elif command.lower() == 'report':
		print(df)
	elif command.lower() == 'add':
		entries()
	elif command.lower() == 'info':
		while True:
			whichstudent = input("Please enter the student ID: ")
			if whichstudent not in StudentDict2['ID']:
				print ("\nStudent doesn't exist, try again\n")
			else: 
				index  =  StudentDict2['ID'].index(whichstudent)
				print (studentinfo(StudentDict2['ID'][index],StudentDict2['Name'][index],StudentDict2['Age'][index],StudentDict2['Major'][index])+ "\n")
				break
	else:
		print("Unknown Command. Please try again")