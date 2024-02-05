import pandas as pd

review = pd.read_csv('./ReviewContent.csv')
'''
print(type(review))
print()
print(review.info())
print()
print(review.head())
print()
print(review.tail()) 

print(review.dtypes)
print(review.ndim) # Boyutları gösterir satır ve sütün olmak üzere 2 boyut

print(review.columns) 
print(review.memory_usage())
print(review["Room Price"].sum()) 
print(review["Room Availability"])
print(review["Room Availability"].sum()) 

print(review["Room Availability"])
print(review["Room Availability"].add(10)) # her eleman degerine 10 ekler
print(review["Room Availability"] + 10) #Series nesnesi integer sayi ile toplanabilir ayni sonucu verir


print(review["City"].value_counts())
print(review["Room Price"].value_counts())
print(review["Room Price"].sort_values(ascending=False))  '''
