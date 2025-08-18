def ride_service():
    while True: 
        print("\--Welcome to Ride Service--")
        print("press 1: book a ride")
        print("press 2: check fare rate")
        print("press 3: view current service")
        print("press 4: Exit")

        choice = int(input("Enter your choice (1-4)"))

        if choice == 1:
            distance = float(input("enter distance in km: "))
            print("your ride is confirmed for", distance, "km.")
        elif choice == 2:
            print("Fare rate is 100 rupees per km.")
        elif choice == 3:
            print("current service car, bike , rickshaw.")
        elif choice == 4:
            print("Thank you for using our service.goodbye")
            break 
        else:
            print("invalid choice, please try again.")
#function call
ride_service()























