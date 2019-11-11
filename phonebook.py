PhoneBook2 = {"user1": "111-111-111" "email:user1@gmail.com" ,"user2": "222-222-222"  "email:user2@gmail.com","user3": "333-333-333","user4": "444-444-444","user5": "555-555-555"}

#def searchbook()
def search():
   searchname = input("Enter User Name: ")
   searchresult = PhoneBook2.get(searchname)
   #searchresult.lower()
   if searchresult  == None:
       print("%s is not in the phonebook" % searchname)
   else:
       print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
       print(f'@@@@@ SEARCH RESULT: {searchname} phone is {PhoneBook2[searchname]} @@@@@@@')
       print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
       print (".")
       print (".")

PhoneBook1 = {"User6": "666-666-666","User7": "777-777-777","User8": "888-888-888","User9": "999-999-999"}

def adduser():
   user = input("Please enter new user name: ")
   newphone = input("Enter phone number: ")
   PhoneBook2[user] = newphone


def deleteuser():
   user = input("Please enter name to delete: ")
   if user in PhoneBook2:
       del PhoneBook2[user]
   else:
       print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
       print(f'{user} not in the phonebook')
       print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


while True:
   print ("#################################")
   print ("***  Yellow Pages Phone Book  ***")
   print ("#################################")
   print ("")
   print ("[1] Search name")
   print ("[2] Add new phone entry:")

   print ("[3] Delete entry:")
   print ("[4] List all phone number entries")
   #print ("[5] Insert email entry:")

   print ("[5] Quit")
   print ("")
   print ("Please enter your selection: ")
   selection = input()

   if selection  == "1":
       search()
   if selection  == "2":
       adduser()
   if selection  == "3":
       deleteuser()
   if selection == "4":
       print(PhoneBook2)
   if selection  == "5":
       print ("See you again! Don't drink and drive!")
       break
   else:
       print("PLEASE enter valid choices (1-5)")
