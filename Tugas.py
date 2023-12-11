import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
print("DataFrame Awal:")
print(df)

# loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for i, row in df.iterrows():
    df.at[i, 'Gaji'] = (lambda x: x + x * (5/100))(row['Gaji'])

print("\nDataFrame Setelah Peningkatan 5% Gaji:")
print(df)

# loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for i, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[i, 'Gaji'] = (lambda x: x * (1 + 2/100))(row['Gaji'])

print("\nDataFrame Setelah Peningkatan Gaji Tambahan:")
print(df)
