"""
1. String should not be empty
2. Email should have @ symbol
3. Password should have special characters, Numbers, Upper chars & Lower chars
"""

import string


# ---------------------- Model ----------------------

class FormField:
    def __init__(self, value_label, field_type):
        self.value_label = value_label
        self.field_type = field_type


# ---------------- Password Validation ----------------

def password_validators(str_input):

    has_special = any(char in string.punctuation for char in str_input)
    has_numbers = any(char in string.digits for char in str_input)
    has_upper = any(char in string.ascii_uppercase for char in str_input)
    has_lower = any(char in string.ascii_lowercase for char in str_input)

    is_pwd_valid = (
        has_special
        and has_numbers
        and has_upper
        and has_lower
    )

    return is_pwd_valid


# ---------------- Input Validation ----------------

def enter_value(value_label="Name", field_type="String"):

    for i in range(3):

        str_input = input(f"Enter {value_label}: ")

        if str_input == "":
            print("Please enter a valid input")
            continue

        if field_type == "Email":

            if "@" not in str_input:
                print("Please enter a valid input, which contains @")
                continue

        if field_type == "PWD":

            is_pwd_valid = password_validators(str_input)

            if not is_pwd_valid:
                print(
                    "Please enter a valid password, "
                    "which contains Special Character, "
                    "Number, Uppercase and Lowercase letter."
                )
                continue

        if field_type == "Gender":

            if str_input.lower() not in [
                "male",
                "female",
                "other",
                "m",
                "f",
                "o"
            ]:
                print("Please enter Male, Female or Other")
                continue

        print(f"This is {field_type} type field.")
        print(f"Entered value is: {str_input}")

        break


# ---------------- Form ----------------

def get_form_values():

    models = [

        FormField("Name", "String"),

        FormField("Email", "Email"),

        FormField("Password", "PWD"),

        FormField("Gender", "Gender"),

        FormField("Is Adult", "Check Box"),

        FormField("Sign In", "Button")

    ]

    for model in models:

        enter_value(
            model.value_label,
            model.field_type
        )


# ---------------- Start Program ----------------

get_form_values()