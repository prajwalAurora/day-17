import pandas as pd
data = {
    "Name":["adg","skfeg","kueg"],
    "Age":[23,32,43],
    "City":["delhi","mumbai","kolkata"]
 }
df = pd.DataFrame(data)
print(df)

df["Bonus"] = df ['Age'] *0.1
print(df)
