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
            break


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


get_cust_info()
accommodation()
print(name, surname, cust_email, cust_phone)
