import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('company-survey')

QUESTIONS = SHEET.worksheet('info')


def get_employee_dept():
    """
    Gets the departments which the employee
    works under
    """
    while True:
        print("Please state what department you currently work for?")
        print("(Digital, Finance, HR, Legal, Production)\n")

        dept = input("Enter your department here: \n")

        if validate_dept(dept):
            break

    return dept


def validate_dept(dept):
    """
    Checks to make sure user entered a valid department.
    Responds with an error if not
    """
    all_depts = ["digital", "finance", "hr", "legal", "production"]

    if dept.lower() in all_depts:
        print("\nThank you for your selection.\n")
        return True
    else:
        print("\nIncorrect department, please choose a relevant department.\n")
        return False


def question_one():
    """
    Gets the employee's rating to question one from the spreadsheet
    """
    print("Please answer the following questions with a rating of 1-5")
    print("1 being strongly disagree(negative)")
    print("5 being strongly agree(positive).\n")

    while True:
        question = QUESTIONS.cell(2,2).value
        q_one = input(f"{question}:\n")  
        if validate_answer(q_one):
            break
    return q_one


def question_two():
    """
    Gets the employee's rating to question two from the spreadsheet
    """
    while True:
        question = QUESTIONS.cell(3,2).value
        q_two = input(f"{question}:\n")  
        if validate_answer(q_two):
            break
    return q_two


def validate_answer(values):
    """
    Checks to make sure answer is between 1 and 5
    Raises ValueError if answer cannot be converted into int,
    or if there isnt't exactly 1 value.
    """ 
    try:
        if len(values) > 1:
            raise ValueError(
                f"Exactly 1 value required, you provided {len(values)}"
            )
        value = int(values)
        if value not in range(1, 6):
            raise ValueError("Answer must be between 1 and 5")
        return True
    except ValueError as e:
        print(f"Invalid input: {e}\n")
        return False


def main():
    """
    Run all program functions
    """
    # user_dept = get_employee_dept()
    # ans_one = question_one()
    question_two()


print("Welcome to our company survey.\n")
main()
