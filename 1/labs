# string='ЖКВИУКУЭВГЦПАНИШЕЧКЙЧЪЪАЬЭЙЭИКАМАВШКЖЪВГЦПЭБВЖКЖИУЭЪВГЦПШЦКЪЙЭЩЧАЬЭЕКАМАВШКЖИЗЖГФЯЖЪШКЭГЧ' 
# a='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' 
# result='' 
# for i in range(len(a)-1): 
#   for letter in string: 
#     result+=a[(a.index(letter)+i)%len(a)] 
#   result+=" "+str(i)+"\n"
# print(result)

import numpy as np
from textwrap import wrap
alph='АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ' 
key='МАТЕРИЯ' 
string1='КОД ПЛЕЙФЕЙЕРА ОСНОВАН НА ИСПОЛЬЗОВАНИИ МАТРИЦЫ БУКВ'.replace(' ','').replace('Ъ','Ь').replace('Й','И').replace('Ё','Е') 
string2='УЕНАЕЭМЧЗПФТКСЪИАРУЕПЕСЯЕХТИСЩГХМЖФЗЧБГЩКМЮАЕЪ'.replace('Ъ','Ь').replace('Й','И').replace('Ё','Е') 

def key_matrix(key,alph):
  temp = list(key)
  for char in alph:
    if (key.find(char) == -1):
      temp += char;
  array=np.array(temp).reshape(5,6)
  return array

# matrix=([
#         ['М', 'А', 'Т', 'Е', 'Р', 'И'],
#         ['Я', 'Б', 'В', 'Г', 'Д', 'Ж'],
#         ['З', 'К', 'Л', 'Н', 'О', 'П'],
#         ['С', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
#         ['Ш', 'Щ', 'Ь', 'Ы', 'Э', 'Ю']
# ])

def index(array, item): 
    for idx, val in np.ndenumerate(array):
        if val == item:
            return idx

def get_string(array):
  str=''
  for i in array:
    str+=i
  return str

def code(m,s):
  bigramm=wrap(s,2)
  result=list()
  for i in bigramm:
    a,b=index(m,i[0]) #поиск в матрице 1 буква в биграмме
    c,d=index(m,i[1]) #поиск в матрице 2 буква в биграмме
    #print(i) # все биграммы
    #print(a,b,c,d)
    if (b==d):
      result.append(m[(a+1)%5][b]+m[(c+1)%5][d])
    elif (a==c):
      result.append(m[a][(b+1)%6]+m[c][(d+1)%6])
    else:
      result.append(m[a][d]+m[c][b])
  print(get_string(result))
 

def decode(m,s):
  bigramm=wrap(s,2)
  result=''
  for i in bigramm:
    a,b=index(m,i[0]) #поиск в матрице 1 буква в биграмме
    c,d=index(m,i[1]) #поиск в матрице 2 буква в биграмме
    #print(i) # все биграммы
    #print(a,b,c,d)
    if (b==d):
      result+=m[a-1][b]+m[c-1][d]
    elif (a==c):
      result+=m[a][b-1]+m[c][d-1]
    else:
      result+=m[a][d]+m[c][b]
  print(result)

matrix=key_matrix(key,alph)
print(matrix)
code(matrix,string1)
decode(matrix,string2)
