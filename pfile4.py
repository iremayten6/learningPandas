import pandas as pd

students = [
    {
        'name': 'arin',
        'age': 21,
        'gender': 'F'
    },
    {
        'name': 'ibrahim',
        'age': 24,
        'gender': 'M'
    },
    {
        'name': 'selin',
        'age': 28,
        'gender': 'F'
    }
]
print(students)
print((type(students)))
df_students = pd.DataFrame(students)
print(df_students)
print(type(df_students))
# klasik dict'ten DataFrame OLUSTURULAMAZ
student = {"Hale": pd.Series(data=[25,"F","CE",56],index=["age","gender","department","height"]),
          "Ahmet": pd.Series(data=[21,"M","EEE",78],index=["age","gender","department","height"]),
          "Fatma": pd.Series(data=[40,"F","EEE",60],index=["age","gender","department","height"])
          }
#print(student)
#print(type(student))

df_stuent = pd.DataFrame(student) # PD SERIES'TEN DATAFRAME OLUSTURDUK
print(df_stuent)
#print(type(df_stuent))
#DATAFRAME İNDEX BELIRLERKEN BILESKEYİ ALIR NaN veri olmadığını  ifade eder
print()

df_student2 = pd.DataFrame(student,columns=["Hale","Ahmet"]) #SATIRA ULASMAK ICIN INDEX KULLANILIR
print(df_student2)
print()
#SATIR VE SUTUNLARI OLUSTURMA

df_students3 = pd.DataFrame(student, columns=["Hale","Ahmet"], index=["department","height"])
print(df_students3)
print()
print(df_stuent[ ["Ahmet","Hale"] ])
print(type(df_stuent[ ["Ahmet","Hale"] ]))
print(df_stuent.loc["age"])
print(df_stuent.loc["department"])
print(df_stuent.loc[["age","gender","height"]])

#DF [col][row]

print(df_stuent["Hale"][0]) #Direkt olarak index de yazılabilir.print(df_stuent["Hale"]["age"]) ile ayni ciktiyi verir
print()

df_stuent["Fatih"] = [30,"M","CE",89]
print(df_stuent)
 # pop sadece column
 # drop column and row

df_stuent.pop("Ahmet")
print(df_stuent)

df_stu = df_stuent.drop(["Hale","Fatma"],axis=1)  #Degiskene atamadan print(df_stuent.drop(["Hale","Fatma"],axis=1)) seklinde de yazilir
print(df_stu)
