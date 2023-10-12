# Input section that takes all the customer details
# Constructing the personal variables

def camping():
    standard_pitch = 1
    secluded_pitch = 2
    yurt = 3

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










print("\n\nWelcome to the Sustainability Booking System\n")
while True:
    try:
        cust_first_name = input("Please enter customer first name: ")
        cust_second_name = input("Please enter customer second name: ")
        cust_email = input("Please enter email address: ")
        cust_phone = input("Please enter phone number: ")
        print(f"\n\nThe details you have entered are:\n"
              f"Name - {cust_first_name} {cust_second_name}\n"
              f"Email - {cust_email}\n"
              f"Phone Number - {cust_phone}")
        confirm = input("\nPlease confirm these details are correct? (y/n): ")

        if confirm.lower() == "y":
            print("\nThank you!")
            break
        else:
            print("Please re-enter the customer details.")
    except:
        continue

# Number of people and nights
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
