import os
# list_paths=[]

# for adress, folder, file in os.walk('C:\\Users\Zver\Desktop'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_paths.append(full_path)

# Creates if it is not and writes to file text
# r=open('text.txt','w')
# r.write('string text')
# r.close

# Reading file.
# r=open('text.txt')
# u = r.read()
# print(u)
# r.close

# r = open('text.txt','w')
# for x in list_paths:
#     r.write(x + '\n')
# r.close 
#
#     
# r = open('text.txt')
# for i in r:
#     if 'text' in i:
#         print(i)
# r.close    

r= open('e.exe','rb')
y= open('Копия e.exe','wb')
while True:
    var = r.read(1048576) #1024*1024 bate read по 1 kB
    print(var.__sizeof__()) # Show file size
    if var.__sizeof__() == 33: 
        break
    y.write(var)   

print('Контрол')
r.close
y.close


