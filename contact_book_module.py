import time


# CONTACT BOOK BLUEPRINT
class ContactBook:
    database = []

    def __init__(self, fname, lname, phone, email, country):

        # instance variables
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.country = country

    def add_contact_detail(self):  # this adds a new contact
        details = [self.fname, self.lname, self.email, self.phone, self.country]
        self.database.append(details)
        return 'Contact added successfully!!!'

    def find_contact_details(self, first_name):  # search for contact and returns None if not found
        for data in self.database:
            for detail in data:
                if first_name == detail:
                    return data
                else:
                    continue

    def update_contact_details(self, x, y, z):  # change details
        # x = reps contact detail you wish to update
        # y = reps data you want to remove from the contact detail
        # z = reps data you want to replace with
        for data in self.database:
            for detail in data:
                if x == detail:
                    print()
                    print('OLD: ', data)
                    break

            index = 0
            for detail in data:
                if y == detail:
                    data[index] = z
                    print('Updating...\n')
                    time.sleep(3)
                    print('NEW: ', data, end='\n')
                    print('Updated successfully!!!')
                    break
                else:
                    index += 1
                    continue

    def delete_contact_details(self, first_name):  # remove from saved contacts
        for data in self.database:
            for detail in data:
                if first_name == detail:
                    print('Deleting...\n')
                    print(f'{data}\n')
                    time.sleep(3)
                    print('deleted successfully\n')
                    self.database.remove(data)

    def list_saved_contacts(self):  # list all saved contacts
        print()
        print('These are your saved contacts: \n')
        counter = 1
        while counter < len(self.database) + 1:
            for data in self.database:
                print(f'{counter}. {data}')
                counter += 1
