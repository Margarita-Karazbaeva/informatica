import sys
ftxt = sys.argv[1]
f = open(ftxt,'r')
total = 0
count = 0
for x in f:
    total += float(x)
    count += 1
f.close()
pre = total/count
pro=round(pre,2)
print("average="+pro)


