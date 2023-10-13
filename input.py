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

# ROOM TYPES
double_room = [3, 7]
triple_room = [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15]
family_room = [4, 5]

# CAMPING PITCHES
standard_pitch = [1, 2, 3, 4, 5, 6, 7, 8]
secluded_pitch = ["Forget Me Knot", "Bramble", "Oak"]

# YURTS
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
                with open("customer_list.txt","a") as f:
                    f.write(name + " " + surname + " " + cust_email + " " + cust_phone + "\n")
                break
            else:
                print("Please re-enter the customer details.")
        except ValueError:
            continue


# Number of people and nights
def accommodation():
    global number_of_nights
    global number_of_people
    global accommodation_type

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
    global camping_type
    print("\nWhat type of camping do you want?"
          "\n1 - Standard camping pitches"
          "\n2 - Secluded pitches"
          "\n3 - Yurts")
    while True:
        try:
            camping_type = int(input("\nSelect 1,2 or 3: "))
            if camping_type < 4:
                break

        except ValueError:
            print("\nPlease enter a number!")

    print("Cheers!")


# Get Lodge information
def lodge():
    global lodge_type
    print("\nWhat type of room do you want?"
          "\n1 - Double room"
          "\n2 - Triple room"
          "\n3 - Family room")
    while True:
        try:
            lodge_type = int(input("\nSelect 1,2 or 3: "))
            if lodge_type < 4:
                confirm = input(f"You want to book a {lodge_type} room for {number_of_people} people. Correct? y/n: ").lower()
                if confirm == "y":
                    print("Awesome!")
                    break
                else:
                    print("Please choose again -")
                    continue

        except ValueError:
            print("\nPlease try again!")


        if confirm == "y":
            print("Awesome!")
            break
        else:
            print("Please enter y or n: ")
            continue


get_cust_info()
accommodation()
print(f"\n\nName - {name, surname}"
      f"\nEmail/Phone number - {cust_email, cust_phone}"
      f"\nNumber of nights - {number_of_nights}"
      f"\nNumber of people - {number_of_people}"
      f"\nAccommodation type - {accommodation_type}"
      f"\nCamping type - {camping_type}"
      f"\nLodge type - {lodge_type}")
