import pandas as pd
data = {
    "Name":["adg","skfeg","kueg"],
    "Age":[23,32,43],
    "City":["delhi","mumbai","kolkata"]
}
df = pd.DataFrame(data)
print(df)
# df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)  