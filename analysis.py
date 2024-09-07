import pandas as pd

##Loading the data##
df = pd.read_csv('inpatient.csv')

##Print rows of data##
#print(df.head())

##View codex columns##
codex_columns = [col for col in df.columns if 'ICD' in col or 'DRG' in col or 'HCPCS' in col]

##Print columns of codex data#
print(codex_columns)

df = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv')
df
