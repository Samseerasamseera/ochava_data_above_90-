import pandas as pd

df = pd.read_excel(r"C:\Users\User\Downloads\41586_2022_5575_MOESM5_ESM.xlsx", sheet_name=1)


percentile_columns = [col for col in df.columns if col.endswith('_percentile')]

pivoted_data = []

for idx, row in df.iterrows():
    for percentile_col in percentile_columns:
        kinase_name = percentile_col.split('_')[0]  
        phosphosite = row['Phosphosite']
        specified_value = row[percentile_col]
        Gene = row['Gene']
        windo_seq = row['SITE_+/-7_AA']
        Uniprot = row['Uniprot']

        
        pivoted_data.append([kinase_name, phosphosite, specified_value,Gene,windo_seq,Uniprot])

pivoted_df = pd.DataFrame(pivoted_data, columns=['Kinase', 'Phosphosite','Specified_Values','Gene','SITE_+/-7_AA','Uniprot'])
pivoted_df = pivoted_df[pivoted_df['Specified_Values'] >= 85]

output_file_path = 'ST_kinases.xlsx'
pivoted_df.to_excel(output_file_path, index=False)


print(f"Filtered data (Specified_Values >= 90) saved to '{output_file_path}'")
