import operator
d={1:2,3:4,4:3,2:1,0:0}
print('original dictionary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('dictionary in ascendind order by value:',sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('dictionary in decending order by value:',sorted_d)