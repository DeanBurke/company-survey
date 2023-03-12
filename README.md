# Company Survey

[View the live project here.](https://company-survey.herokuapp.com/)

![Screeshot of the site on Am I repsonsive](./assets/images/am-i-responsive.jpg)

Welcome to our company survey! We are excited to hear your feedback and opinions on your experience at our company. Your responses will help us to better understand how we can improve our workplace and make it a better environment for employess.

This survey will ask you a series of questions related to various aspects of your experience with the company. Please make sure to read each question carefully and to select the answr that best reflects your experience. 

Thank you in advance for taking the time to complete this survey. Your feedback is greatly appreciated and will help us make positive changes within the company.

---

# Program intended use

![Screeshot of the site on flowchat](./assets/images/flowchart.jpg)

The Python program developed is designed to gather valuable feedback from employees.

The program begins by asking employees to input their department, and then asks them five questions that require a rating between 1 and 5. Once employees have submitted their responses, the program automatically pushes the information to a Google Sheet, where the responses are compiled and averaged per department on a separate sheet.

This updated average is sent back to the terminal, to give employees an up to date rating per department before the deadline is finished and the results will be announced. 

---

# Features

* The program will only allow the employee to select from a select number of departments.
    * An error message is returned if the employee tries to input incorrect department, or misspells one the departments that is an option.
    * It won't matter if the employee uses any capital letters, the program will accept the entry once it is spelt correctly.
    * It will loop until a correct option is enterend.
* The program then asks the five questions, it will only accept an answer between 1 and 5.
    * It will raise a ValueError and display a message to the terminal if the employee tries to enter a number higher, more than one digit/character or is a letter.
    *  It will loop until a correct option is enterend.
* The program then creates a user submission string (converting the answers into integers) and pushes it to the Google Sheet.
* The program then pulls the updated information from the 'average' tab on the Google Sheet and calls it to the terminal. 
* Goodbye message then runs and program ends. 
