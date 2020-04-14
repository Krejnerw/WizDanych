zakupy = {"mleko":"litr","bulki":"sztuki","marchew":"sztuki"}
L2=[ x for x in zakupy if zakupy[x]=="sztuki"]
print(L2)

# odwrocenie
# L3=[zakupy[x] for x in zakupy if x=="mleko"or x=="marchew"]
# print(L3)
