stored_username = "admin" 
stored_password = "admin"
max_attempts = 3

for attempt in range(max_attempts):
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    if username_input == stored_username and password_input == stored_password:
        print("Login successful!")
        break  # Exit the loop if credentials match
    else:
        remaining_attempts = max_attempts - attempt - 1
        print("Incorrect credentials. Attempts remaining:", remaining_attempts)

else:  # Executed if the loop completes without hitting 'break' 
    print("Account locked: Too many failed attempts.")

 