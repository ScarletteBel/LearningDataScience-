## Scarlette Bello Barron       c0860234

def dictCreator():
    with open('ContactManager.txt', 'r') as f:
        lines = f.readlines()

    myDict = {}
    for i in range(0, len(lines), 3):
        index = i
        name = lines[i].replace("\n", "")
        email = lines[i+1].replace("\n", "")
        phoneNumber = lines[i+2].replace("\n", "")

        myDict[name] = {'email': email, 'phoneNumber': phoneNumber, 'index': index}

    return myDict


def initialList():
    myDict = dictCreator()
    myList = list(myDict.keys())

    for i in range(len(myList)):
        print(f'{i+1}.- {myList[i]}')


def view():
    myDict = dictCreator()

    for name in myDict.keys():
        print(f"number: {int(myDict[name]['index']/3 + 1)}")
        print(f'name: {name}')
        print(f"email: {myDict[name]['email']}")
        print(f"phone number: {myDict[name]['phoneNumber']}")

def add():
    name = input("Insert the name contact you want to add: ")
    email = input("Insert the email contact you want to add: ")
    phoneNumber = input("Insert the phone number contact you want to add: ")

    with open('ContactManager.txt', 'a') as f:
        f.write(f"{name}\n{email}\n{phoneNumber}\n")

def search():
    myDict = dictCreator()

    target = input("Insert the name you want to delete: ")

    for name in myDict.keys():
        if name == target:
            return True, myDict[name]["index"], target
    return false, -1, target

def delete():
    myDict = dictCreator()
    flag, index, target = search()
    if flag:
        with open('ContactManager.txt', 'w') as f:
            for name in myDict.keys():
                if name != target:
                    f.write(f"{name}\n{myDict[name]['email']}\n{myDict[name]['phoneNumber']}")




print("Welcome to your Contact Manager! \n Please choose one option of the next available menu (type the key word)")

print("List - display your contacts")
print("View - view your contacts")
print("Add - add a new contact")
print("del - delate a contact")
print('\n')

action = input("Insert the command for using your Contact manager: ")


if action.lower() == "list":
    initialList()
elif action.lower() == "view":
    view()
elif action.lower() == "add":
    add()
elif action.lower() == "del":
    delete()







