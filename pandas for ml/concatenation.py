import pandas as pd
df_Region1 = pd.DataFrame({
    'CustumerID':[1,2,3],
    'Name':['fhrr','wkejf','oewrh']
})
df_Region2 = pd.DataFrame({
    'CustumerID':[4,5,6],
    'Name':['giurh','irg','rghr']
})
df_concat = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concat)