
# Technical Documentation – Personal Finance Manager

## Project Architecture
The application follows a modular architecture where each component has a specific responsibility.

### Components
- main.py – Application entry point
- Expense – Represents a single expense record
- ExpenseManager – Handles user interaction and logic
- FileManager – Handles CSV read/write and backup
- Reports – Generates analytical reports
- Utils – Input validation and text cleaning

## Data Structures Used
- List: Stores expense objects
- Dictionary: Stores category-wise and month-wise totals
- CSV File: Persistent storage of expense data

## Algorithms Implemented
- Summation algorithm for total expenses
- Dictionary grouping for category-wise expenses
- Date slicing for monthly reports
- File copy operation for backup

## Error Handling
- Invalid date formats are rejected
- Invalid or negative amounts are not accepted
- User input is validated using utility functions

## Technical Requirements Fulfilled
- Expense class with required attributes
- CSV-based file handling
- Modular code organization
- Automatic backup feature
- Input validation and exception handling

## Scalability
The modular structure allows easy addition of:
- Database support
- GUI interface
- Advanced analytics
