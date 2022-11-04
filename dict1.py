dict1={'name':'Raji' ,'age':20 ,'address':'kizhakkedathu house'}
print(dict1)
dict2=dict1.copy()
print(dict2)
print("value=" ,dict1.values())
print("keys=" ,dict1.keys())
dict3={'aadhar':1234567}
dict1.update(dict3)
print(dict1)