def check_eligibility(name, age, citizen):
    if age >= 18 and citizen == "y":
        print(name, "is eligible to vote.")
        return True
    else:
        print(name, "is not eligible to vote.")

        if age < 18:
            print("Years left to become eligible:", 18 - age)

        if citizen == "n":
            print("Reason: Not an Indian citizen.")

        if age < 18 and citizen == "n":
            print("Reason: Under 18 and not an Indian citizen.")

        return False


voters_checked = 0
eligible_count = 0
not_eligible_count = 0

while True:
    name = input("Enter your name: ").strip()

    while name == "":
        print("Invalid name. Please enter your name.")
        name = input("Enter your name: ").strip()

    while True:
        try:
            age = int(input("Enter your age: "))

            if age < 0 or age > 120:
                print("Invalid age. Age must be between 0 and 120.")
                continue

            break

        except ValueError:
            print("Invalid input. Enter a whole number.")

    citizen = input("Indian citizen (y/n): ").strip().lower()

    while citizen not in ("y", "n"):
        print("Invalid input. Enter y or n.")
        citizen = input("Indian citizen (y/n): ").strip().lower()

    result = check_eligibility(name, age, citizen)

    voters_checked += 1

    if result:
        eligible_count += 1
    else:
        not_eligible_count += 1

    another = input("Check another voter? (y/n): ").strip().lower()

    while another not in ("y", "n"):
        print("Invalid input. Enter y or n.")
        another = input("Check another voter? (y/n): ").strip().lower()

    if another == "n":
        break

print("Voters checked:", voters_checked,
      "| Eligible:", eligible_count,
      "| Not eligible:", not_eligible_count)