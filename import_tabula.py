import tabula
import pandas as pd
from tabula.io import read_pdf


def pdf_to_excel(pdf_file_path, excel_file_path):
    # Read PDF file
    tables = tabula.io.read_pdf(pdf_file_path, pages='all')


    # Write each table to a separate sheet in the Excel file
    with pd.ExcelWriter(excel_file_path) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f'Sheet{i+1}')




pdf_to_excel('C:\\Users\\mewah\\Downloads\\Bank_statement.pdf', 'C:\\Users\\mewah\\Downloads\\Excel_file.xlsx')
