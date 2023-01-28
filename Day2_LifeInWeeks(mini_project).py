
MAX_AGE=90

# Type and bound check.
while True:
    try:
        age = int(input("What is your current age? (between 0 and 90): "))
        # Exit loop only if no exception and criteria is meet.
        if 0<= age <=90:   
            break   
        else:
            print("Age must be between 0 and 90. Please try again!")
    except ValueError:
        print("Age must be an integer. Please try again!")


years_left=MAX_AGE-age
months_left=years_left*12
weeks_left=years_left*52
days_left=years_left*365

message=(
    f"You have {days_left} days or {weeks_left} weeks or " 
    f"{months_left} months left until you reach {MAX_AGE} years old"
    )


print(message)