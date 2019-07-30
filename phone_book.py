import json
f = open("book.txt","w")
phone_book = {}
command = ""
while command != 'exit':
    command = input('Enter a command(options: new,get,save,del): ')
    if command == "new":
        name = input('Enter name of the person: ')
        if name in phone_book:
            print('Already Present')
        else:
            p = input('Phone number: ')
            a = input('Address: ')
            phone_book[name] = {'phone': p, 'address': a}
    elif command == 'get':
        name = input('Enter name of the person')
        if name in phone_book:
            print(phone_book[name])
        else:
            print('Person not found in Address Book')
    elif command == 'del':
        name = input('Enter the Name of the Person: ')
        del phone_book[name]
    elif command == 'save':
        s=json.dumps(phone_book)
        with open("book.txt","w") as f:
            f.write(s)
        #f.write(json.dumps(phone_book))
