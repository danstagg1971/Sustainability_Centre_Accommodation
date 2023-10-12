# Input section that takes all the customer details

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




print("End")

