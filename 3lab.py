import numpy as np

alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
string_code='ПЕЛЬМЕШКИ'
key_word='ДВЕ'

def code(alf,key,string):
  answer=[]
  for index in range(len(string)):
    i=alf.find(string[index])
    j=alf.find(key[index%len(key)])
    answer.append((i+j)%32)
  return answer

def decode(alf,key,string):
  answer=[]
  for index in range(len(string)):
    i=alf.find(string[index])
    j=alf.find(key[index%len(key)])
    answer.append((i-j)%32)
  return answer

def tsiferki_bukofki(alph,inds):
  shifr=[]
  for i in inds:
    shifr.append(alph[i])
  shifr=''.join(shifr)
  return shifr

indexs=code(alphabet,key_word,string_code)
print(indexs)

answer=tsiferki_bukofki(alphabet,indexs)
print(answer)

first_indexs=decode(alphabet,key_word,answer)
print(first_indexs)

first_string=tsiferki_bukofki(alphabet,first_indexs)
print(first_string)
