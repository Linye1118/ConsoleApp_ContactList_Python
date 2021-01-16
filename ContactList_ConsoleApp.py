
class Person(object):
    def __init__(self, FirstName, LastName, PhoneNumber, Email, Addresses, Type):
        self.FirstName = FirstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Addresses = Addresses  
        self.Type = Type

fileName = "ContactList.txt"
People = []
from itertools import islice
def loadData():
    #fileName = "ContactList.txt"
    lineNr = 8    
    try:
        with open(fileName, 'r') as fp:
            while True:
                count = 0
                tmp_lines = list(islice(fp, lineNr))
                
                if not tmp_lines:
                    break
                for line in tmp_lines:
                    # test print...
                    # print(line.strip())
                    count += 1                    
                    if count==8:
                        addresses = []
                        addresses.append(tmp_lines[4])
                        addresses.append(tmp_lines[5])
                        new = Person(tmp_lines[0],tmp_lines[1], tmp_lines[2],
                                     tmp_lines[3],addresses,tmp_lines[6])                                    
                        People.append(new)                                              
    except FileNotFoundError:
        print('No existing file')
    finally:
        print(fileName + 'load sucess!\n')
        
loadData()

def addPerson():
    while True:
        FirstName = input("Enter first name: ")or '(null)'
        LastName = input("Enter last name: ")or '(null)'
        PhoneNumber=input("Enter phone number: ")or '(null)'
        Email = input("Enter email: ")or '(null)'

        Addresses = []
        Addresses.append(input("Enter 1st address: ")or '(null)')
        Addresses.append(input("Enter 2nd address(optional): ")or '(null)')
        Type = input("Enter type/remark(optional): ")or '(null)'

        if FirstName=='(null)' and LastName=='(null)':
            print("First Name/Last Name cannot be all null")
            
        elif PhoneNumber=='(null)' and Email=='(null)' and Addresses[0]=='(null)' and Addresses[1]=='(null)':
            print('Phone Nr/Email/Address cannot be all null')
            
        else:
            new = Person(FirstName,LastName, PhoneNumber, Email, Addresses, Type)
            People.append(new)
            print("New contact created!\n", '-------------------------')
            printPerson(new)
            print(' -------------------------\n', str(len(People))+' contacts in the list')
            break

def printPerson(person):
    print("First Name: " + person.FirstName.strip())
    print("Last Name: " + person.LastName.strip())
    print("Email: " + person.Email.strip())
    print("Phone Number: " + person.PhoneNumber.strip())
    print("Address 1: " + person.Addresses[0].strip())
    print("Address 2: " + person.Addresses[1].strip())
    print("Type/Remark: " + person.Type)
   
def listPeople():
    print(str(len(People))+' contacts in the list.')
    i = 1
    for it in People:
        print('Contact# ' + str(i))
        printPerson(it)
        print('---')
        i += 1
    print('----------- End -------------\n')

def searchPeople():
    UserInput = input ("Enter the first name of the person you would find: ")
    listFound = []
    count = 1
    for x in People:
        if x.FirstName.strip() == UserInput.strip():
            print("Search result#: " + str(count))
            printPerson(x)
            listFound.append(x)
            count += 1
    if len(listFound)==0:
            print("Name could not be found: " + UserInput)
            
    return listFound    

def deletePerson():
    listTarget = searchPeople()
    if len(listTarget) == 0: return      
    else:
        x = input("Please select the number to remove or type A to remove all...")
        if x!= "A" and x.isdigit():
            index = int(x)-1
            if index >=0 and index < len(listTarget):
                p = listTarget[index]
                People.remove(p)
                print("Person removed.")
            else:
                print("Invalid number choice...(number out of range)")
                return
        elif x=="A":
            for it in listTarget:
                People.remove(it)
                print("Person removed.")            
        else:
            print("Invalid selection...(number or A)")
            return     
       

def editPerson():
    print()
    
def saveFile():
    with open("TestSave.txt",'w') as fp:
        for it in People:
            fp.write(it.FirstName)
            fp.write(it.LastName)           
            fp.write(it.PhoneNumber)
            fp.write(it.Email)
            fp.write(it.Addresses[0])
            fp.write(it.Addresses[1])
            fp.write(it.Type)
            fp.write('---\n')


UserMenu = '''
    ======================================
    . add
    . delete
    . list
    . edit
    . search
    . exit
    ======================================
'''
commands = {'add': addPerson, 'delete': deletePerson, 'list': listPeople,
            'edit': editPerson, 'search': searchPeople, 'exit': saveFile}

print('Welcome to contact list!\n', UserMenu)
cmd = input('Enter command: ')    
while cmd!= 'exit': 
    if cmd in commands:
        commands[cmd]()
    else:
        print('Choice cannot be found' + cmd)        
    print(UserMenu)
    cmd = input('Enter command: ') 
if cmd=='exit':
    print('Good Bye')
