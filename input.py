# Input section that takes all the customer details

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


# Get customer personal details
def get_cust_info():
    global name
    global surname
    global cust_email
    global cust_phone

    print("\n\nWelcome to the Sustainability Booking System\n")

    while True:
        try:
            name = input("Please enter customer first name: ")
            surname = input("Please enter customer second name: ")
            cust_email = input("Please enter email address: ")
            cust_phone = input("Please enter phone number: ")
            print(f"\n\nThe details you have entered are:\n"
                  f"Name - {name} {surname}\n"
                  f"Email - {cust_email}\n"
                  f"Phone Number - {cust_phone}")
            confirm = input("\nPlease confirm these details are correct? (y/n): ")

            if confirm.lower() == "y":
                print("\nThank you!")
                with open("customer_list.txt", "a") as f:
                    f.write(name + " " + surname + " " + cust_email + " " + cust_phone + "\n")
                break
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
            elif camping_type == 2:
                camping_type = secluded_pitch[0]
            elif camping_type == 3:
                camping_type = yurts
            else:
                continue
            confirm_camping = input(
                f"You want to book a {camping_type} for {number_of_people} people. Correct? y/n: ").lower()
            if confirm_camping == "y":
                print("Awesome!")
                break
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
            if lodge_type == 1:
                lodge_type = double_room[0]
            elif lodge_type == 2:
                lodge_type = triple_room[0]
            elif lodge_type == 3:
                lodge_type = family_room[0]
            else:
                continue
            confirm_lodge = input(
                f"You want to book a {lodge_type} room for {number_of_people} people. Correct? y/n: ").lower()
            if confirm_lodge == "y":
                print("Awesome!")
                break
        except ValueError:
            print("\nPlease try again!")





get_cust_info()
accommodation()
print(f"\n\nName - {name, surname}"
      f"\nEmail/Phone number - {cust_email, cust_phone}"
      f"\nNumber of nights - {number_of_nights}"
      f"\nNumber of people - {number_of_people}"
      f"\nAccommodation type - {accommodation_type}"
      f"\nCamping type - {camping_type}"
      f"\nLodge type - {lodge_type}")
