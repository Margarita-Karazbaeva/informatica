a=str(input("Введите последовательность ДНК:"))
A=0
T=0
G=0
C=0
for i,j,k,l in a:
    if i=='A':
        A=A+1
    if j=='T':
        T=T+1
    if k=='G':
        G=G+1
    if l=='C':
        C=C+1
print(A+" "+T+" "+G+" "+C)