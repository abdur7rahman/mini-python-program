# Open the Document in Read Format 
doc = open("sample.txt","r")
# Read the Text in a Document
content = doc.read()
# Split the Statements in Document by using a Single White Space ' '
count = content.split(' ')
# print the Total count of word in a Document by len()
print(len(count)) # 219