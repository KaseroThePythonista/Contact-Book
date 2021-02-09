# IMPORTING PERSON MODULE

from contact_book_module import ContactBook
import time

# ###################### START OF DEFAULTS ################### #

# fname, lname, phone, email, country
de = ['steve', 'kasero', '0700675766', 'kaserosteve@gmail.com', 'kenya']
de2 = ['ben', 'munene', '0708837675', 'danphotoart4@gmail.com', 'ethiopia']
de3 = ['peter', 'merisho', '0714827155', 'merishopeter@gmail.com', 'uganda']

c_book = ContactBook(de[0], de[1], de[2], de[3], de[4])
c_book2 = ContactBook(de2[0], de2[1], de2[2], de2[3], de2[4])
c_book3 = ContactBook(de3[0], de3[1], de3[2], de3[3], de3[4])

c_book.add_contact_detail()
c_book2.add_contact_detail()
c_book3.add_contact_detail()

# ####################### END OF DEFAULTS ##################### #

while True:
    print()
    print('          CONTACT BOOK.\n')
    print('     1. Add contact.')
    print('     2. Search contact.')
    print('     3. Update contact.')
    print('     4. List all contacts.')
    print('     5. Delete contact.')
    print('     6. EXIT PROGRAM\n')
    print('          SELECT ANY OPERATION.\n')

    selection = input('Type here: ')

    if selection == '1':
        print()
        fname = input('first name: ')
        lname = input('last name: ')
        phone = input('phone number: ')
        email = input('email address: ')
        country = input('country: ')
        print()

        new_entry = ContactBook(fname, lname, phone, email, country)
        results1 = new_entry.add_contact_detail()
        print(results1)
        time.sleep(5)
        continue

    elif selection == '2':
        print()
        key_word = input('Type the first name of whom you wish to search: ')
        results2 = c_book.find_contact_details(key_word)
        if results2 is None:
            print('Contact not found in database!!!')
        else:
            print(results2)

        time.sleep(5)

        continue

    elif selection == '3':
        x = input('f_name of the contact you with to update: ')

        results3 = c_book.find_contact_details(x)
        if results3 is None:
            print('Contact not found in database!!!')
        else:
            print(results3)

        y = input('contact detail you wish to update: ')
        z = input('new contact detail: ')

        c_book.update_contact_details(x, y, z)
        time.sleep(5)
        continue

    elif selection == '4':
        c_book.list_saved_contacts()
        time.sleep(5)
        continue

    elif selection == '5':
        key_word2 = input('Type the f_name to delete the contact detail: ')
        c_book.delete_contact_details(key_word2)
        time.sleep(5)
        continue

    elif selection == '6':
        print('The program is shutting down in five seconds. Please wait!!!')
        time.sleep(5)
        break
