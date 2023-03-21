from src.controller.contacts_controller import ContactsController

if __name__ == "__main__":
    try:
        token = 'pat-eu1-9492283a-09bc-4833-9dca-8c643d662007'
        contacts = ContactsController.get_contacts(token)
        print("Get_Contacts: " + list(contacts))
    except Exception as e:
        print("Error: " + str(e))
