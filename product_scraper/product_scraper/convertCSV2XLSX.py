import pandas as pd
read_file = pd.read_csv (r'out_dunlopsports.com.vn_thoitrangnam.csv')
read_file.to_excel (r'out_dunlopsports.com.vn_thoitrangnam.xlsx', index = None, header=True)