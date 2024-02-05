import pandas as pd

review = pd.read_csv("./ReviewContent.csv")
''' 
print(review) 
print(review["Country"])
print(type(review["Country"])) 
# upper(), lower(), len(), title()
print(review["Country"].str.upper()) # degisiklikler inplace seklinde olmaz inplace islemini assignment yaparak gerceklestirir

review["Country"] = review["Country"].str.upper()
print(review["Country"])
#print(review["Country"].str.lower())
#print(review["Country"].str.title ()) 

print(len(review["Country"])) #satir sayisi
print(review["Country"].str.len()) # iceriklerin uzunlugu 

# replace()
print(review["Room Type"].str.replace("room","Room")) 

print(review["City"].str.upper().str.contains("YORK")) # T-F olarak deger dondurur
mask = review["City"].str.upper().str.contains("YORK")
print(review[mask])

mask = review["City"].str.upper().str.startswith("LOS")
print(review[mask]) # endswith sonu bitenlere bakar 
# strip() bastaki ve sondaki boslukları yok eder
# split() stringleri bolumlere ayırır ve list seklinde geri doner
print("irem-kerim-iso".split("-")) 

print(review["City"].str.split(" ").str.get(0)) '''
print(review["City"].str.split(" ",expand=True)) # list seklinde degil df seklinde doner.
print(type(review["City"].str.split(" ",expand=True)))

