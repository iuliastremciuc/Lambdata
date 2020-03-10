# my_lambdata/my_script.py
from my_lambdata.my_mod import enlarge
import pandas
print("Hello")

df = pandas.DataFrame({"state": ["CT", "CO", "AZ"]})
print(df.head())

print("---------")

x = 5
print("num", x)
print("enlarged num", enlarge(x))