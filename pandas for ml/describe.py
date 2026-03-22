import pandas as pd
data = {
    "Name":["adg","skfeg","kueg"],
    "Age":[23,32,43],
    "City":["delhi","mumbai","kolkata"]
 }
df = pd.DataFrame(data)
print("sample data frame")
print(df)
print("descriptive statistics of dataset")
print(df.describe())