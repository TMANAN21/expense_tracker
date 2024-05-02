# expense_tracker
It tracks where you spend the most money, as well as, categorizes your expenses.

- The program reads your bank statements(pdf files) and converts it into a CSV file
- Creates a single DataFrame that contains all the expenses from different vendors/sources
- The CSV file then makes an API call to OpenAI by sending the expense descriptions to obtain the correct category
- Assigns the suggested categories to the corresponding rows in the DataFrame and exporting the result to an Excel file
