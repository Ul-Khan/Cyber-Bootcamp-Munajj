while True:
    try:
        user_input = input("enter a number: ")
        number = int(user_input)
        print("you entered:", number)
        break # Exit loop if conversion succeeds
    except ValueError:
        print("Invalid input. Please enter a number.")





        result = s.connect_ex(("localhost", 443))
print("Port open" if result ==0 else "Port Closed")
