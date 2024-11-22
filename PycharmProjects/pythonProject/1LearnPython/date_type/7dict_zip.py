l1 = ['zs', 'ls', 'ww']
l2 = list(range(23, 26))

d1 = {keys: val for keys, val in zip(l1, l2)}
print(d1)



for m, n in zip('123', 'ABC'):
 print(m , ':' , n)