import pandas as pd
data = {
    "Name":["adg","skfeg","kueg"],
    "Age":[23,32,43],
    "City":["delhi","mumbai","kolkata"]
 }
df = pd.DataFrame(data)
print(df)

df.loc[0,"Age"] = 24
print(df)