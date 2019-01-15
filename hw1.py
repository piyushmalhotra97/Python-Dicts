d1={'name':'welcome','age':46}
d2={'name':'hi','age':36,'sex':'m'}
d3={'name':'born','age':676,'color':'fair'}

print 'length of d2:%d'%len(d2)
print 'length of d3:%d'%len(d3)

d4=d3.copy()
print d4
d3.clear()
print d3

d5={'name':'reborn','age':'unknown'}
d6={'color':'black'}

d3.update(d5)
print d3
d2.update(d6)
print d2
print 'length of d2:%d'%len(d2)
print 'compare13:%d'%cmp(d1,d3)
print 'compare24:%d'%cmp(d2,d4)
print type(d4)
print d3.items()
print d1.keys()
print d4.values()

