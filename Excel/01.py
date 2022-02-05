import pandas as pd

b = input('Besin: ')

# print ile 'df' i yazdırırsan tüm veriler düzenli bir şekilde gelir. 

df = pd.read_excel('veri.xlsx',engine='openpyxl')



result = df.groupby('Besin')

print(result.get_group(b).mean())



# Burada elinle manual olarak istediğin besin bilgilerini alabilirsin.

# print(result.get_group('Bıldırcın').mean())

