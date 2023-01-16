def main():
    welcome()
    list_options=["1","2","3","4","5"]
    option="y"
    while option=="y":
        option=input("type an option: ")
        option=validate_option(option, list_options)
        if option in list_options:
            if option=="1":
                view_all_devices()
                option=input("\nDo you want to continue(y/n)?: ")
                option=validate_input(option)
                if option=="y":
                    print("\nSelect one option from the list ( 1, 2, 3, 4, or 5): ")
            elif option=="2":
                add_device()
                option=input("\nDo you want to continue(y/n)?: ")
                option=validate_input(option)
                if option=="y":
                    print("Select one option from the list ( 1, 2, 3, 4, or 5): ")
            elif option=="3":
                delete_device()
                option=input("\nDo you want to continue(y/n)?: ")
                option=validate_input(option)
                if option=="y":
                    print("Select one option from the list ( 1, 2, 3, 4, or 5): ")
            elif option=="4":
                update_device()
                option=input("\nDo you want to continue(y/n)?: ")
                option=validate_input(option)
                if option=="y":
                    print("Select one option from the list ( 1, 2, 3, 4, or 5): ")
            elif option=="5":
                break
        else:
            print('\nThis is an invalid selection, try again')
            option=input("Do you want to continue(y/n)?: ")

    print("\nThanks for using the application")

def welcome():
    print("Welcome to the Devices Management System\n")
    print("Select one option from the list ( 1, 2, 3, 4, or 5): ")
    print("\n 1. view all devices\n 2. add a device\n 3. delete a device\n 4. update a device\n 5. exit the program\n")

def view_all_devices():
    print("\n")
    with open("devices.txt") as file:
        file = file.readlines()
        for f in range(len(file)):
            file[f]=file[f].replace("\n","")
        for e,l in enumerate(file):
            print(str(e+1)+".", l)

def add_device():
    print("\n")
    with open("devices.txt", "a") as file:
        new_device=input("type the new device: ")
        file.write("\n"+new_device)
    print("{} is added".format(new_device))

def delete_device():
    print("\n")
    num_delete=int(input("type the number's device to delete: "))
    with open("devices.txt", "r") as file:
        list = file.readlines()
        del list[num_delete-1]
    with open("devices.txt", "w") as file:
        for w in list:
            file.write(w)
    print("Device #{} Deleted".format(num_delete))

def update_device():
    print("\n")
    num_update=int(input("type the number's device to update: "))

    with open("devices.txt", "r") as file:
        list = file.readlines()
    new_name=input("type de device name: ")
    list[num_update-1]=new_name+"\n"
    with open("devices.txt", "w") as file:
        for w in list:
            file.write(w)
    print("Device #{} updated".format(num_update))

def validate_input(option):
    while option != "y" and option !="n":
        print("This is an invalid answer, try again.")
        option=input("Do you want to continue(y/n)?: ")
        print(option)
    return option

def validate_option(option, list_options):
    while option not in list_options:
        print("This is an invalid option, try again.")
        option=input("Select one option from the list ( 1, 2, 3, 4, or 5): ")
    return option


if __name__=="__main__":
    main()
