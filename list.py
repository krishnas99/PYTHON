lst=[1,3,5,9,11,34]
lst1=[3,13,5,7,20,65]
s=int(0)
c=int(0)
for i in lst and lst1:
    if len(lst)==len(lst1):
        print("list area of same length")
        break
    else:
        print("list have different length")
        break
for i in range(0,len(lst) and len(lst1)):
    s=s+lst[i]
    c=c+lst1[i]
for i in range(0,len(lst) and len(lst1)):
    if s==c:
        print("sum of values are same")
        break
    else:
        print("sum of values are different")
        break
print("elements that matched are:")
l=[]
for i in range(0,len(lst)):
    for j in range(0,len(lst1)):
        if lst[i]==lst1[j]:
            l.append(lst[i] and lst1[j])
        else:
            p=i
            continue
print(l)