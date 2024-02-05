import pandas as pd

print(pd.__version__)
person = {'ad': ['burak','ayse','fatma','irem','kerim'],
          'yas': [29,20,25,30,35],
          'maas': [5000,60000,70000,30000,900000]}

#Series tek boyutlu
#DataFrame çok boyutlu

df = pd.DataFrame(person)
print(df)
print()

student = pd.Series(data =["Arin",23,"CE"],index = ["name","age","department"])
student.name = "İREM"

X = "irem" in student.values
print(X)
print(student)
print(type(student))
print(student.ndim)
print(student.size)
print(student.name)
print(student.dtype)
print(student.shape)
print(student.index)
print(student.values)

# mean() ortalama
# product() carpma