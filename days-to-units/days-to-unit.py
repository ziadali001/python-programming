def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def input_validation():
    try:
        user_input_number = int(days_and_units_dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            the_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(the_value)
        elif user_input_number == 0:
            print("you entered invalid value")
        else:
            print("you entered invalid value")
    except ValueError:
        print("you entered invalid value")


user_input = ""
while user_input != "exit":
    user_input = input("enter the value!\n")
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    input_validation()

