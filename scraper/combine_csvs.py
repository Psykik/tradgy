import os
import glob
import pandas as pd

os.chdir("./csv")
files = [i for i in glob.glob('*.csv')]

combined_csv = pd.concat([pd.read_csv(f) for f in files if f != "combined.csv"]) # combine all files in the list
combined_csv.to_csv("combined.csv", index=False, encoding='utf-8-sig') # export to csv

#combined_csv = combined_csv.query("place != ''") # filter by place
combined_csv = combined_csv[combined_csv["place"].notna()]
combined_csv.to_csv("combined.filtered.csv", index=False, encoding='utf-8-sig') # export to csv