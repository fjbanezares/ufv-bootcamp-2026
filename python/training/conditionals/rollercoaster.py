# We start by welcoming the user to our rollercoaster program.
print("Welcome to the rollercoaster!")

# We then ask the user for their height in centimeters.
height = int(input("What is your height in cm? "))

# We initialize the bill variable to 0, which will hold the cost for the user.
bill = 0

# We check if the user's height is greater than or equal to 120 cm.
if height >= 120:
    # If the user's height is above 120 cm, they are allowed to ride the rollercoaster.
    print("You can ride the rollercoaster!")

    # We then ask the user for their age to determine the ticket price.
    age = int(input("What is your age? "))

    # If the user's age is below 12, they are considered a child and are charged $5.
    if age < 12:
        bill = 5
        print("Child tickets are $5.")

    # If the user's age is between 12 (exclusive) and 18 (inclusive), they are considered a youth and are charged $7.
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    # If the user is older than 18, they are considered an adult and are charged $12.
    else:
        bill = 12
        print("Adult tickets are $12.")

    # After determining the ticket price, we ask if the user wants a photo.
    wants_photo = input("Do you want a photo taken? Y or N. ")

    # If the user wants a photo (indicated by "Y"), we add $3 to their bill.
    if wants_photo == "Y":
        bill += 3

    # Finally, we print out the total cost for the user.
    print(f"Your final bill is ${bill}")

# If the user's height is below 120 cm, they are not allowed to ride the rollercoaster.
else:
    print("Sorry, you have to grow taller before you can ride.")
