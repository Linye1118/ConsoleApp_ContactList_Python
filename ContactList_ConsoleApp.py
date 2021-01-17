
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
                        addresses.append(tmp_lines[4].strip())
                        addresses.append(tmp_lines[5].strip())
                        new = Person(tmp_lines[0].strip(),tmp_lines[1].strip(), tmp_lines[2].strip(),
                                     tmp_lines[3].strip(),addresses,tmp_lines[6].strip())                                    
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
    print("Type/Remark: " + person.Type + "\n")
   
def listPeople():
    print(str(len(People))+' contacts in the list.')
    i = 1
    for it in People:
        print('Contact# ' + str(i))
        printPerson(it)
        print('***')
        i += 1
    print('----------- End -------------\n')

def searchPeople():
    UserInput = input ("Enter the first name/start letter of the contact to search: ")
    listFound = []
    count = 1
    for x in People:
        #if x.FirstName.lower().strip() == UserInput.lower().strip():
         if x.FirstName.lower().strip().startswith(UserInput.lower().strip()):
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
        x = input("\nSelect the number to remove or type A to remove all...")
        if x.isdigit():
            index = int(x)-1
            if index >=0 and index < len(listTarget):
                p = listTarget[index]
                People.remove(p)
                print("Person removed.")
            else:
                print("Invalid number ...(number out of range)")
                return
        elif x.lower()=="a":
            for it in listTarget:
                People.remove(it)
                print("Person removed.")            
        else:
            print("Invalid selection...(number or type A)")
            return     
       

def editPerson():
    print("Not impelemented...")
    
def saveFile():
    with open(fileName,'w') as fp:
        for it in People:
            fp.write(it.FirstName + '\n')
            fp.write(it.LastName + '\n')      
            fp.write(it.PhoneNumber + '\n')            
            fp.write(it.Email + '\n')
            fp.write(it.Addresses[0] + '\n')
            fp.write(it.Addresses[1] + '\n')
            fp.write(it.Type + '\n')
            fp.write('***\n')

    print("...data saved...")

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

print('******Welcome to contact list!******\n', UserMenu)
cmd = input('Enter command: ').lower()   
while cmd!= 'exit': 
    if cmd in commands:
        commands[cmd]()
    else:
        print('Command cannot be found ' + cmd)        
    print(UserMenu)
    cmd = input('Enter command: ') 
if cmd=='exit':
    commands[cmd]()
    print('Good Bye')
