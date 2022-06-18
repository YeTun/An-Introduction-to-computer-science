# Me Computer, Mandalay.
# June 23, 2022
# exercise_3.py

''' Write a program to keep track of conference attendees. For each attendee, your program
should keep track of name, company, state, and email address. Your program should allow users to do things such as add a new attendee, display information on an attendee, delete an attendee, list the names and email addresses of all attendees, and list the names and email addresses of all attendees from a given state. The attendee list should be stored in a file and loaded when the program starts.'''

'''
TODO: delete attendee
TODO: list the names and email addresses
TODO: list the names and email addresses from specific state
TODO: display information about specific attendee
'''

'''
data: we can store the data in a list to access information about the attendees
'''

conferenceAttendees = []
class Attendee:

    def __init__(self,name,company,state,email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email
    
    def getName(self):
        return self.name
    
    def getCompany(self):
        return self.company
    
    def getState(self):
        return self.state
    
    def getEmail(self):
        return self.email

    def displayNamesAndEmail(self):
        for att in conferenceAttendees:
            print(att.getName(), att.getCompany(),att.getState(),att.getEmail())
            
    def filterNamesAndEmail(self,s):
        for att in conferenceAttendees:
            if att.getState() == s:
                print(att.getName(), att.getCompany(),att.getState(),att.getEmail())                                

    def displayInformation(self,n):
        # loop through to find the attendee
        for att in conferenceAttendees:
            if att.getName() == n:
                # if there is a match print the information
                print(att.getName(),att.getCompany(),att.getState(),att.getEmail())
            else:
                print('Sorry we could not find that attendee.')

def addAttendee():
        # Will need user input for the different parameters to initialize a class
        n = input('Enter the name of the attendee: ')
        c = input('Enter the name of the company for the attendee: ')
        s = input('Enter the state where the attendee lives: ')
        e = input('Enter the attendees email: ')
        return Attendee(n, c, s, e)

def deleteAttendee(n):
        # loop through list containing attendees
        for att in conferenceAttendees:
            # find name in list
            if att.getName() == n:
                # remove if found
                conferenceAttendees.remove(n)
                print('Successfully removed {} from the list.'.format(n))
            else:
                print('We could not find that attendee, sorry.')

def main():
    print('Welcome to the conference. What would you like to do?')
    while True:
        print('1: Add Attendee\n2: Delete Attendee\n3: Display information for specific attendee\n4: Names and Emails of all Attendees\n5: Search for names and emails in a specific state\n6: Exit')
        choice = input(': ')
        if choice == '1':
            person = addAttendee()
            conferenceAttendees.append(person)
            print(conferenceAttendees)
        elif choice == '2':
            n = input('Which attendee would you like to remove? >> ')
            deleteAttendee(n)
        elif choice == '3':
            n = input('Which perons information would you like to see? >> ')
            for att in conferenceAttendees:
                if att.getName() == n:
                    print(att.getName(),att.getCompany(),att.getState(),att.getEmail())
            else:
                print('Sorry could not find that person.')
        elif choice == '4':
            for att in conferenceAttendees:
                print(att.getName(),att.getCompany(),att.getState(),att.getEmail())
        elif choice == '5':
            s = input('Enter the state you\'d like to view: ')
            for att in conferenceAttendees:
                if att.getState() == s:
                    print(att.getName(), att.getCompany(),att.getState(),att.getEmail()) 
            else:
                print('Sorry there is either nobody in that state here, or there was a typo.')
        else:
            return False

main()