a=str(input("Введите последовательность ДНК:"))
A=0
T=0
G=0
C=0
for i in a:
    if i=='A':
        A=A+1
for j in a:
    if j=='T':
        T=T+1
for k in a:
    if k=='G':
        G=G+1
for l in a:
    if l=='C':
        C=C+1
print(str(A)+" "+str(T)+" "+str(G)+" "+str(C))