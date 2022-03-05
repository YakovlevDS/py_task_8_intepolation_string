# s='Let\'s write a string as s'
# d="Let\'s write a string 'as' s"
# k="Let\'s write \n a string 'as' s"
 # url="https:\\www.youtube.com\\new"
# url=r"https:\\www.youtube.com\new"  #r --игнорировать 

# print(s)
# print(d)
# print(k)
# print(url)

s='string text'
print(s.upper())
print(s.lower())
print(s.capitalize())


pathLin = 'C:/User/Py/Desktop/str.py'
pathWin = pathLin.replace('/','\\') 
print(pathWin)

r=pathWin.split('\\')
print(r[-1]) # получение имени файла
