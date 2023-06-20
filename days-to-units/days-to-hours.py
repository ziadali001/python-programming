calculation_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def input_validation():
    try:
        user_input_number = int(num_of_elements)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            the_value = days_to_units(user_input_number)
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
    list_of_days = user_input.split()
    for num_of_elements in set(list_of_days):
        input_validation()

