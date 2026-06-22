l=[2,4,5,3,6,"hi","Mom","dad",True,False]
inte=[]
st=[]
bol=[]
for words in l:
    if type(words)==int:
        if words%2!=0:
            inte.append(words)
    elif type(words)== str:
        if words[:].lower()==words[::-1].lower():
            st.append(words)
    elif type(words)==bool:
        if words==True:
            bol.append(words)

result=inte+st+bol
print(result)
