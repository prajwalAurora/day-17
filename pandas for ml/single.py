import pandas as pd
data = {
    "Name":["adg","skfeg","kueg"],
    "Age":[23,32,43],
    "City":["delhi","mumbai","kolkata"]
    }
df = pd.DataFrame(data)
print("sample data frame")
print(df)
print("Names (single column return as series)")
name = df["Name"]
print(name)