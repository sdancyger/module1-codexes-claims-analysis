import pandas as pd

dataset_path = 'inpatient.csv'
df = pd.read_csv(dataset_path)

print(df.head())
codex_columns = ['ICD_code_1', 'ICD_code_2', 'DRG_code', 'HCPCS_code_1']

for column in codex_columns:
    if column in df.columns:
        print(f"\nAnalyzing column: {column}")

        value_counts = df[column].value_counts(dropna=False)
        print(f"Value Counts for {column}:\n{value_counts}")

        missing_values = df[column].isnull().sum()
        print(f"Missing values in {column}: {missing_values}")

       df[column].fillna('Unknown', inplace=True)
    
        updated_value_counts = df[column].value_counts()
        print(f"Updated Value Counts for {column}:\n{updated_value_counts}")
    else:
        print(f"Column {column} not found in dataset.")

df.to_csv('cleaned_inpatient.csv', index=False)

print(df.columns)
