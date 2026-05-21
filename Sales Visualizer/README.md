# Sales Analyzer

## Features
- Load sales data from CSV file
- Display dataset preview
- Show dataset information and statistics
- Handle missing values by filling with 0
- Sort data by selected column
- Filter data based on column values
- Calculate sum and mean of a column
- Visualize data with bar charts
- Exit option for program termination

## Program Flow
1. Display main menu
2. User selects an option:
   - **Option 1:** Load data from CSV
   - **Option 2:** Show dataset preview
   - **Option 3:** Show dataset info
   - **Option 4:** Show dataset statistics
   - **Option 5:** Handle missing values
   - **Option 6:** Sort data
   - **Option 7:** Filter data
   - **Option 8:** Calculate sum and mean
   - **Option 9:** Plot data
   - **Option 10:** Exit program
3. Execute the selected functionality
4. Show results or confirmation messages
5. Continue until user chooses to exit

## Concepts Used
- Pandas for data loading, cleaning, and analysis
- Matplotlib for data visualization
- DataFrame operations (`head`, `info`, `describe`, `isnull`, `fillna`, `sort_values`, filtering)
- Statistical calculations (`sum`, `mean`)
- Loops (`while`) for menu-driven interface
- Conditional statements (`if`, `elif`, `else`) for option handling
- User input handling (`input()`)
- Exception handling (`try`, `except`)
