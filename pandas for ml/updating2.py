import pandas as pd
data = {
    "Name":["adg","skfeg","kueg"],
    "Age":[23,32,43],
    "City":["delhi","mumbai","kolkata"]
 }
df = pd.DataFrame(data)
print(df)

# df["Age"] = df["Age"] * 1.05
df.loc[0,"age"] = 45
print(df)