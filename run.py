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


def get_employee_dept():
    """
    Gets the departments which the employee
    works under
    """
    while True:
        print("Welcome to our comppany survey.\n")
        print("Please state what department you currently work for?")
        print("(Digital, Finance, HR, Legal, Production)\n")

        dept = input("Enter your department here: \n")
        
        if validate_dept(dept):
            print("Data is valid")
            break


def validate_dept(dept):
    """
    Checks to make sure user entered a valid department.
    Responds with an error if not
    """
    all_depts = ["digital", "finance", "hr", "legal", "production"]

    if dept.lower() in all_depts:
        print("Thank you for your selection.\n")
        return True
    else:
        print("Incorrect department, please choose a relevant department.\n")
        return False


get_employee_dept()