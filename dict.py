d1={'a':7}
d2=dict(a=7)
d3=dict.fromkeys([1,2,3,4,5,6,7,8,9,10],'val')
price={'meat':3,'bread':1,'potato':10,'milk':7,'water':4,'oil':.1,'fish':0.5}
users={
    'Jack':{'password':345345,'id':1},
    'Jain':{'password':1345,'id':2},
    'Juice':{'password':2222,'id':3},
}


def buy():
    to_pay = 0
    while True:
        enter = input( 'What we buy???\n')
        if enter=='end':
            break
        to_pay += price[enter]
    return to_pay 

print(d1)    
print(d1['a']) 
d1['v'] =23 
print(d1) 

del d1['v']
print(d1) 
print(d2) 
print(d3)

print(buy())

