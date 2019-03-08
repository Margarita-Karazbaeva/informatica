a=str(input("введите последовательность ДНК:"))
b=a[::-1]
c=b.replace("A","B")
d=c.replace("T","A")
e=d.replace("G","E")
f=e.replace("C","G")
g=f.replace("B","T")
h=g.replace("E","C")
print (h)