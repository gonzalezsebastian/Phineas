import pandas as pd
#pip install openpyxl

interval = pd.read_excel('input_output.xlsx',sheet_name='Sample Input', index_col=0)
print (interval)
