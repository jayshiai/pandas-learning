import pandas as pd

df = pd.read_csv('./pokemon_data.csv')

df_xls = pd.read_excel('./pokemon_data.xlsx')

df_txt = pd.read_csv('./pokemon_data.txt', delimiter="\t")

# read columns
# print(df.columns)

# read each columns
# print(df[['Name', 'Type 1', 'HP']][4:5])

# Get data of specific index - iloc[]
# print(df.iloc[1:4])

# Read from a specific location (R,C)
# print(df.iloc[2,1])

# Read each Row

# for index, row in df.iterrows():
# print(index, row['Name'])

# finding data with specific values in it with - loc
# print(df.loc[df['Type 1'] == 'Fire'])

# get some statistical data like mean and stuff with - describe
# print(df.describe())

# SORTING
# print(df.sort_values('Name', ascending=False))
# somewhat complex sorting
# print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0])) #sorts with Type 1 primarily in ascending order and with HP in descending order


# CHANGING DATA

# adding a column Total wit sum of other columns

# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + \
#     df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.head(5))

#  removing a column
# df = df.drop(columns=['Total'])
# print(df.head(5))

# another way of declaring a column
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df)

# rearranging columns
# df = df[['#', 'Name', 'Type 1', 'Type 2', 'Legendary', 'Total', 'HP',
#       'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']]

# print(df)

# shorter way of doing above rearrangement will be

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(df)


# SAVING OUR DATA .. index = False means there won't be 0,1,2,3.. before every entry in csv
# df.to_csv('modified.csv', index=False)

# to excel
# df.to_excel('new.xlsx', index=False)

# to txt
df.to_csv('modifer.txt', index=False, sep="\t")
