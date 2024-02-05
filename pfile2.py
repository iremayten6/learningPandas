import pandas as pd

student = pd.Series(['Arin','Software','23',"CE"],["name","surname","age","department"])

print(student),
print()
print(student[["name","age"]])
print()
print(type(student[["name","age"]]))

print(student[[0,2]])
print(student[0:4])
print(student[-2])
print(student[0:])
print(student["name":"department"])

#loc- location , iloc-index location

print(student.loc["department"])
print(student.iloc[3]) #string olarak girilirse hata verir
print()
# PANDAS SERIES YAPISI DEĞİŞTİRİLEBİLER(MUTABLE)

student["name"] = "ELIS"
student.iloc[2] = 16

print(student)
student.drop("name",inplace=True) #NAME VERİSİNİ OLDUĞU YERDE BASKA DEĞİŞKENE ATAMADAN SİLDİ
print(student)




