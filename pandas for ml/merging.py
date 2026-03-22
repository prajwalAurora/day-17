import pandas as pd
df_custumer = pd.DataFrame({
    "CustomerId":[1,2,3],
    "Name":["lkgr","ejrh","jrg"]

})
df_order = pd.DataFrame({
    "CustomerId":[1,2,3],
    "OrderId":[123,456,789]
})
df_merged = pd.merge(df_custumer,df_order,on="CustomerId",how="right")
print('right join')
print(df_merged)
