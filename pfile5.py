import pandas as pd


student = {"Hale": pd.Series(data=[25, "Aslan","F","CE",56],index=["age","surname","gender","department","height"]),
          "Ahmet": pd.Series(data=[21,"M","EEE",78],index=["age","gender","department","weight"]),
          "Fatma": pd.Series(data=[40,"Sanlıer","EEE",160],index=["age","surname","department","height"])
          }
df_stuent = pd.DataFrame(student) #NaN ifadesi eksik  veriyi ifade eder
print(df_stuent)
print()
'''
#ISNULL()

x = df_stuent.isnull()
print(x)
print(type(x))
print()
y = df_stuent.isnull().sum()
print(y) # kac tane NaN deger vearsa onun sayisini gösterir ve dönüs seri seklinde olur
print(type(y))
print()
z = df_stuent.isnull().sum().sum()
print(z)  # toplam kac tane NaN varsa onu gösterir
print(type(z))

#NOTNULL() ISNULL()'IN TAM TERSİ  OLARAK CALISIR TRUE OLANLARI GOSTERİR
#ISNULL İLE NaN DEGER OLUP OLMADIGINI BULURUZ

a = df_stuent.count()
print(a)
print(type(a))
print()
b = df_stuent.count().sum()
print(b)
'''
# dropna()

x = df_stuent.dropna(how="all")
print(x)
print(type(x))
print()   #DROPNA() İLE İCİNDE NaN OLAN İFADEYİ FULL KALDİRİR

df_stuent.dropna()
print(df_stuent) # dropnayı bir degiskene atamamız lazım yokda direkt olarak calısmaz

b = df_stuent.dropna(thresh=2)
print(b) # iki tane NaN olan satırları silme islemi weight satirinda iki tane NaN oldugu için weight satiri  silindi
#axis=1 NaN degeri olan sütunalrı siler

df_stuent.dropna(inplace=True) # NaN degeri olan sütünlari siler
print(df_stuent)