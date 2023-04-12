import os
import pandas as pd

home = os.path.expanduser("~")
downloads = os.path.join(home, "Downloads")
path = os.path.join(downloads, 'icici_auth_fail.csv')

df = pd.read_csv(path)
unique_remarks = df.groupby("Remarks").nunique()
total = unique_remarks.sort_values("ATMID").sum()
print(total)
print(unique_remarks.sort_values('ATMID'))
