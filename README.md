## Project Overview

The Personal Finance Manager is a console-based Python application designed
to help users record, analyze, and manage daily expenses. The project focuses
on clean architecture, object-oriented programming, and reliable data
persistence using CSV files.

The main objective is to demonstrate best practices in Python development,
including modular design, input validation, and separation of concerns.



## Code Structure Explanation

The application follows a modular and object-oriented design:

- `main.py`  
  Acts as the entry point and handles user interaction and menu flow.

- `Expense` class  
  Represents a single expense with attributes:
  date, category, amount, description.

- `ExpenseManager` class  
  Manages business logic such as adding expenses and coordinating
  between user input, validation, and file operations.

- `FileManager` class  
  Handles all file-related operations including loading expenses,
  saving data, and creating backups.

- `Reports` module  
  Contains read-only analytical functions such as total expense,
  category-wise filtering, and monthly summaries.

- `utils` module  
  Centralizes input validation and data cleaning logic.



### Add Expense Feature

The Add Expense feature is implemented using a clean and maintainable
approach. User input is collected through dedicated helper methods
for date, category, amount, and description.

This design ensures:
- Clear separation of input validation and business logic
- Improved readability and maintainability
- Consistent error handling for invalid inputs

The validated data is then encapsulated into an Expense object
and persisted using the FileManager.



## Technical Requirement Mapping

| Requirement | Implementation |
|------------|----------------|
| Expense class with attributes | Implemented in `Expense` class |
| CSV-based persistence | Handled via `FileManager` using `csv` module |
| Error handling | Centralized in `utils` module |
| OOP principles | Used throughout the project |
| Backup mechanism | Automatic CSV backup after save |
| Modular design | Separate modules for logic, IO, and reports |




## Screenshots

Screenshots demonstrating:
- Adding an expense
- Viewing expenses
- Category-wise filtering
- Backup file creation

are available in the `screenshots/` folder.



## Setup and Installation

This project uses only Python standard libraries.
No additional packages are required.


1. Clone the repository:
   git clone <your-github-repo-url>

2. Navigate to the project folder:
   cd personal_finance_manager

3. (Optional) Create virtual environment:
   python -m venv venv
   source venv/bin/activate   (Windows: venv\Scripts\activate)

4. Install dependencies:
   pip install -r requirements.txt

5. Run the application:
   python main.py




## Error Handling and Validation

All user inputs are validated before processing:

- Date validation ensures correct YYYY-MM-DD format
- Amount validation ensures positive numeric values
- Text inputs are cleaned to remove extra spaces and inconsistencies

Validation logic is centralized in the `utils` module,
ensuring consistency and reusability across the application.
