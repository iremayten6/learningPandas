import pandas as pd

review = pd.read_csv("ReviewContent.csv")
'''
print(review)
print(review["City"] == "London") # sehir bilgisi london olanı true verir digerlerini false

print(review[review["City"] == "London"]) 

# duplicated()

review.sort_values("City",inplace=True)
print(review["City"])
print(review["City"].duplicated())
mask = ~review["City"].duplicated()
print(review[mask])  '''

# drop_duplicates() bir satirdaki tüm veriler aynıysa onlari siler
# unique,nunique

