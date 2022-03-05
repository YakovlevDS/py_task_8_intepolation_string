# import time

# def f(*args):
#     list_new=[]
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#         return list_new

# z=list(range(10000))
# x=list(range(5000,15000))
# c=list(range(10000,20000))

# start=time.time()
# f(z,x,c)
# stop=time.time()-start
# print(stop)

# start2=time.time()
# r=set(z)
# t=r.union(set(x),set(c))
# stop2=time.time()-start2
# print(stop2)
# n=stop/stop2
# print('работа с множеством (set) в ',n,'раз быстрее')


# z={1,2,3,4,5,6}
# x={4,5,6,7,8,9,10}
# z.add(7)
# z.discard(1)
# z.remove(3)
# y=z.union(x)
# t=z.intersection(x)#пересечение
# e=z.difference(x)# не перечечения, есть в z но нет в x
# z.update(x)
# print(y)
# print(z)
# print(t)
# print(e)

# получаем уникальные слова с двух тестов
# new =set()
# r1=open('text1.txt')
# new.update(set(r1.read().split()))
# r1.close()
# r2=open('text2.txt')
# new.update(set(r2.read().split()))
# r2.close()
# print(new)

# получаем разницу между двумя тестами
r=open('text1.txt')
r1= set(r.read().split())
r.close()

r=open('text2.txt')
r2=(r.read().split())
r.close()
enter =r1.intersection(r2)
diff = r1.difference(r2)
# new1 = r2.difference(r1)
print(diff)
print(enter)
# print(new1)