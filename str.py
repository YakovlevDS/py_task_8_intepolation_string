# s='Let\'s write a string as s'
# d="Let\'s write a string 'as' s"
# k="Let\'s write \n a string 'as' s"
 # url="https:\\www.youtube.com\\new"
# url=r"https:\\www.youtube.com\new"  #r --игнорировать 

# print(s)
# print(d)
# print(k)
# print(url)

# s='string text'
# print(s.upper())
# print(s.lower())
# print(s.capitalize())


# pathLin = 'C:/User/Py/Desktop/str.py'
# pathWin = pathLin.replace('/','\\') 
# print(pathWin)

# r=pathWin.split('\\')
# print(r[-1]) # получение имени файла


q = open('text.txt', encoding='utf-8')
r1 = (q.read())
q.close()
print(r1)
list_simbol=['(',')','"',',','\n']
for i in list_simbol:
    r1 = r1.replace(i, '')
print(r1)
r2=r1.split()
print(r2)

new_text=' '.join(r2)
print(new_text)