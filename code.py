import re
string=input("enter any sentence")
clean= re.sub(r'[^\w\s]','',string)
print(clean)
