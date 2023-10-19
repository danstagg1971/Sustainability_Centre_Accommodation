from cust_database import CustomerDatabase
from datetime import datetime

today = datetime.today().strftime("%d-%m-%Y")
db = CustomerDatabase()

# Constructing the personal variables
name = "0"
surname = "0"
cust_email = "0"
cust_phone = 0
number_of_nights = 0
number_of_people = 0
accommodation_type = 0
camping_type = 0
lodge_type = 0
confirm_lodge = "0"
confirm_camping = "0"

# ROOM TYPES
double_room = ["Double room", 3, 7]
triple_room = ["Triple room", 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15]
family_room = ["Family room", 4, 5]

# CAMPING PITCHES
standard_pitch = ["Standard pitch", 1, 2, 3, 4, 5, 6, 7, 8]
secluded_pitch = ["Secluded pitch", "Forget Me Knot", "Bramble", "Oak"]

# YURTS
yurts = "Yurt"
yurt1 = ["Rose"]
yurt2 = ["Olive"]
yurt3 = ["Mini"]

# Tariff
standard_pitch_cost = 10
secluded_pitch_cost = 18
rose_cost = 140
olive_cost = 140
mini_cost = 100
lodge_single_cost = 35
lodge_family_cost = 90


# Input section that takes all the customer details
# Get customer personal details
def get_cust_info():
    global name
    global surname
    global cust_email
    global cust_phone

    while True:
        try:
            name = input("\nPlease enter customer first name: ").strip()
            surname = input("Please enter customer second name: ").strip()
            cust_email = input("Please enter email address: ").strip()
            cust_phone = input("Please enter phone number: ").strip()
            print(f"\n\nThe details you have entered are:\n"
                  f"Name - {name} {surname}\n"
                  f"Email - {cust_email}\n"
                  f"Phone Number - {cust_phone}")
            confirm = input("\nPlease confirm these details are correct? (y/n): ")

            if confirm.lower() == "y":
                print("\nThank you!")
                with open("customer_list.txt", "a") as f:
                    f.write(name + " " + surname + " " + cust_email + " " + cust_phone + "\n")
                    item1 = (
                        today,
                        name,
                        surname,
                        cust_email,
                        cust_phone
                    )
                    db.insert(item1)
                accommodation()
                beginning()
            else:
                print("Please re-enter the customer details.")
        except ValueError:
            continue


# Number of people and nights
def accommodation():
    global number_of_nights, number_of_people, accommodation_type

    while True:
        try:
            number_of_nights = int(input("\nNumber of nights: "))
        except ValueError:
            print("Please enter a number")
        else:
            break
    while True:
        try:
            number_of_people = int(input("Number of people: "))
        except ValueError:
            print("Please enter a number")
        else:
            break

    # Accommodation type
    while True:
        try:
            accommodation_type = int(input("\n1 - for Camping"
                                           "\n2 - for Lodge"
                                           "\nSelect 1 or 2: "))
        except ValueError:
            print("Please enter a number")
        else:
            if accommodation_type == 1:
                print(f"\nYou have selected Camping for {number_of_people} people for {number_of_nights} nights")
                camping()
                break
            else:
                print(f"\nYou have selected the Lodge for {number_of_people} people for {number_of_nights} nights")
                lodge()
                break


# get camping information
def camping():
    global confirm_camping, camping_type, standard_pitch, secluded_pitch, yurts, yurt1, yurt2, yurt3
    print("\nWhat type of camping do you want?"
          "\n1 - Standard camping pitches"
          "\n2 - Secluded pitches"
          "\n3 - Yurts")
    while True:
        try:
            camping_type = int(input("\nSelect 1,2 or 3: "))
            if camping_type == 1:
                camping_type = standard_pitch[0]
                camping_standard_calc()
                break
            elif camping_type == 2:
                camping_type = secluded_pitch[0]
                camping_secluded_calc()
                break
            elif camping_type == 3:
                camping_type = yurts
                yurt_calc()
                break
            confirm_camping = input(
                f"You want to book a {camping_type} for {number_of_people} people. Correct? y/n: ").lower()
            if confirm_camping == "y":
                print("Awesome!")
        except ValueError:
            print("\nPlease try again!")


# Get Lodge information
def lodge():
    global lodge_type, confirm_lodge, double_room, triple_room, family_room
    print("\nWhat type of room do you want?"
          "\n1 - Double room"
          "\n2 - Triple room"
          "\n3 - Family room")
    while True:
        try:
            lodge_type = int(input("\nSelect 1,2 or 3: "))
            if lodge_type == 1 and number_of_people <= 2:
                lodge_type = double_room[0]
            elif lodge_type == 2 and number_of_people <= 3:
                lodge_type = triple_room[0]
            elif lodge_type == 3 and number_of_people <= 5:
                lodge_type = family_room[0]
            else:
                print("\nPlease re-enter!\n")
                accommodation()
                beginning()
            confirm_lodge = input(
                f"You want to book a {lodge_type} room for {number_of_people} people. Correct? y/n: ").lower()
            if confirm_lodge == "y":
                print("Awesome!")
                lodge_calc()
                break
        except ValueError:
            print("\nPlease try again!")


# Cost Calculations
def lodge_calc():
    cost = number_of_nights * number_of_people * lodge_single_cost
    print(f"Total cost for {number_of_nights} nights in a {lodge_type}"
          f"\nfor {number_of_people} people is - £{cost}")


def camping_standard_calc():
    cost = number_of_nights * number_of_people * standard_pitch_cost
    print(f"Total cost for {number_of_nights} nights in a standard pitch"
          f"\nfor {number_of_people} people is - £{cost}")


def camping_secluded_calc():
    cost = number_of_nights * number_of_people * secluded_pitch_cost
    print(f"Total cost for {number_of_nights} nights in a secluded pitch"
          f"\nfor {number_of_people} people is - £{cost}")


def yurt_calc():
    while True:
        yurt_type = int(input("\n1 - Rose yurt (up to 5 people)"
                              "\n2 - Olive yurt (up to 5 people)"
                              "\n3 - Mini yurt (up to 2 people)"
                              "\n\nPlease select a yurt: "))
        if yurt_type == 1 and number_of_people <= 5:
            cost = number_of_nights * rose_cost
            print(f"Total cost for {number_of_nights} nights in Rose yurt"
                  f"\nfor {number_of_people} people is - £{cost}")
            break

        elif yurt_type == 2 and number_of_people <= 5:
            cost = number_of_nights * olive_cost
            print(f"Total cost for {number_of_nights} nights in Olive yurt"
                  f"\nfor {number_of_people} people is - £{cost}")
            break
        elif yurt_type == 3 and number_of_people <= 2:
            cost = number_of_nights * mini_cost
            print(f"Total cost for {number_of_nights} nights in Mini yurt"
                  f"\nfor {number_of_people} people is - £{cost}")
            break
        else:
            print("Two many people for this yurt")
            accommodation()
            break



print("\n\nWelcome to the Sustainability Booking System")


def beginning():
    while True:
        try:
            start = int(input("\n1 - booking System"
                              "\n2 - Exit"
                              "\n\nPlease select: "))

            if start == 1:
                get_cust_info()
                break
            elif start == 2:
                print("Bye!")
                quit()
        except ValueError:
            print("Please enter 1 or 2")
            continue


beginning()
