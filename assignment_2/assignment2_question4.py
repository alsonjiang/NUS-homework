def check_age():
    attempts = 1
    while True:
        age = input("Enter age: ")
        if age.isdigit():
            if 1 <= int(age) <= 100:
                print(f"Your age is {age}\nNumber of attempts = {attempts}")
                break
            else:
                attempts += 1
                #print("Please enter an age between 1 and 100 inclusive")
        else:
            attempts += 1
            #print("Please enter a valid number")


check_age()