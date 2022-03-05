
d1={'a':7}
d2=dict(a=10)
d3=dict.fromkeys([1,2,3,4,5,6,7,8,9,10],'val')
price={'meat':3,'bread':1,'potato':10,'milk':7,'water':4,'oil':.1,'fish':0.5}
users={
    'Jack':{'password':345345,'id':1},
    'Jain':{'password':1345,'id':2},
    'Juice':{'password':2222,'id':3},
}

# sale_price={}
# for i in price:
#     sale_price[i]=round(price[i]*0.85, 2)


# print(price)
# print(sale_price)


# for key, value in price.items():
#     print(key)
#     print(value)

# We change the keys and values
new={}
for key, value in price.items():
    new[value]=key
print(new)




