import pandas as pd
import glob

filepaths = glob.glob('Invoices/*.xlsx')

# Debug print to verify the file paths
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)

