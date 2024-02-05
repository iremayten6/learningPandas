import pandas as pd

review_content = pd.read_csv("ReviewContent.csv", usecols=["Review ID"], squeeze=True, encoding="UTF-8", engine="python")
# squeeze true ise series döner false ise dataframe döner.

#print(type(review_content))
#print(review_content.head(10))
#print(review_content.tail(5))
#print(review_content.sort_values().head(10))  # anlik olarak değişiklik yapar orjinal veriyi değiştirmez
review_content.sort_values(inplace=True,ascending=False)#büyükten kücüğe
print(review_content.head(10))
review_content.sort_index(inplace=True)
print(review_content.head(10))
print()
print(type(review_content[4]))
print(type(review_content.get([0,4])))

print(review_content.get([0,4]))


