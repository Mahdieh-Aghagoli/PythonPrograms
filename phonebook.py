def person_information():
    # Receiving and storing personal information
    while True:
        personal_information = {}
        print("Enter new user information:")
        personal_information["name"] = input("Name: ")
        personal_information["surname"] = input("Surname: ")
        personal_information["cell"] = input("Cell: ")
        personal_information["birthday"] = input("Birthday: ")
        personal_information["email"] = input("Email: ")
        if personal_information["name"] == "" and personal_information["cell"] == "":
            print("\n\aFill in the Name or Cell field!!!\n")
        else:
            phone_book.append(personal_information)
            print("\n***information saved***")
            break


def search(item):
    # Searching for the name or cell in the phonebook
    for i in phone_book:
        if i["name"] == item:
            print("\nname:" + item + "\nsurname:" + i["surname"] + "\ncell:" + i["cell"] + "\nbirthday:" + i[
                "birthday"] + "\nemail:" + i["email"])
            return
        elif i["cell"] == item:
            print("\nname:" + i["name"] + "\nsurname:" + i["surname"] + "\ncell:" + item + "\nbirthday:" + i[
                "birthday"] + "\nemail:" + i["email"])
            return
    else:
        print("Not found!!")


def menu():
    # Menu definition
    while True:
        ch = input("\nMENU:\n1.Enter user information\n2.Search\n3.View all informatin\n4.Exit\n")
        if ch == '1':
            person_information()
        elif ch == '2':
            item = input("enter name or cell: ")
            search(item)
        elif ch == '3':
            print(phone_book)
        elif ch == '4':
            break
        else:
            print("\nplease select option of menu!\a\a")


phone_book = []
person_information()
menu()