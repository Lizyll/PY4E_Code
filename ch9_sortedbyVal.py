d = {'b': 123, 'c': 21, 'a': 53}
tmp = list()
for k,v in d.items():
    tmp.append( (v, k) )  #append can only take one. 
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)
