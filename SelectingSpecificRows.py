import pandas as pd

df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/Data_count_state_level.csv')
print(df.head())
print('********************************* READ COMPLETE *********************************')

#selecting rows where party = republican
df_1 = df.loc[df['party']=='republican']
print(type(df_1))
print(df.loc[df['party']=='republican'])

#selecting rows where candidate is donald trump
print(df.loc[df['candidate']=='Donald Trump'])

#selecting rows where votes are greater than 100k
df_3 = df.loc[df['votes_by_party'] > 100000]
print(type(df_3))

print(df_3.head())