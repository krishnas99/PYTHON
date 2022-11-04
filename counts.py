s=input("enter a sentance")
counts=dict()
print(counts)
words=s.split()
print(words) 
for i in words:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1
for k,v in counts.items():
    print(k,v)
 