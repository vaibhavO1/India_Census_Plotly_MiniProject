import numpy as np
import pandas as pd
lat_long = pd.read_csv('district wise centroids.csv')
# print(lat_long.isnull().sum())
# print(lat_long.head())
census = pd.read_csv('india-districts-census-2011.csv')
# print(census.isnull().sum().sum())
# print(census.head())
# print(list(census.columns))
# cols = list(census.columns)[:9]
cols = [
    'District code', 'State name', 'District name', 'Population', 'Male', 'Female', 'Literate', 'Male_Literate', 'Female_Literate',
    'Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains', 'Others_Religions', 'Religion_Not_Stated', 'LPG_or_PNG_Households', 
    'Housholds_with_Electric_Lighting', 'Households_with_Internet', 'Households_with_Computer', 'Rural_Households', 'Urban_Households', 
    'Households'
        ]
# print(cols)
final_df = lat_long.merge(census[cols],left_on='District',right_on='District name').drop(columns=['District name'])
# print(final_df)
final_df['Others_Religions'] = final_df['Others_Religions'] + final_df['Religion_Not_Stated']
# print(final_df['Others_Religions'])
final_df['sex_ratio'] = round((final_df['Female']/final_df['Male'])*1000)
final_df['literacy_rate'] = round((final_df['Literate']/final_df['Population'])*100)
final_df.drop(columns=['Male','Female','Literate','Religion_Not_Stated'],inplace=True)
# print(final_df.shape)
final_df.to_csv('india.csv')