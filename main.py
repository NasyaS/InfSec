import itertools as it
import numpy as np
import re

def get_indexes(key):  # функция для составления словаря 
  inds=[]
  for i in range(len(key)):
   inds.append(key.index(str(i+1)))
  return inds

def cut_string(lst):  # функция для разбиения на символы строк
  temp=[]
  for item in lst:
    temp.append(list(item))
  return temp

def decode(nums, string, key, answer):  
  key=list(key)
  sorted_nums=[]

  for number in nums:  # 1) сортировка по длине ключа
    if number.isdigit() and int(number)>len(key):
      continue
    else:
      sorted_nums.append(number) # убрали элементы больше длины ключа    
  # print(sorted_nums)

  symbols = key.count('X') # 2) составление всех комбинаций с известным ключом
  if symbols==0:
    combs = key 
  else: 
    combs = list(it.permutations(sorted_nums, symbols)) #все комб. из чисел от 1 до длины ключа (7) размера 3 
  print("Число комбинаций с повторами: " + str(len(combs)))

  variants=[]
  for i in range(len(combs)): # 3) подставление этих комбинаций в ключ (столько же)
    temp_key=key.copy()
    if 'X' in temp_key:
      for number in combs[i]:
        j = temp_key.index('X')
        temp_key[j] = number
    variants.append(temp_key)

  sorted_variants=[]  # 4) убираем одинак. цифры в комбинациях, сравниваем с нужной длиной
  for var in variants:
    if len(set(var))==len(key):
      sorted_variants.append(var)
  print("Число комбинаций без повторов: " + str(len(sorted_variants)))

  cut_decode_string=[]  # 5) разрезаем строку на по столбцам
  step=int(len(string)/len(key))
  print("Число строк: " + str(step)) # шаг разреза 
  for i in range(0, len(string), step):
    cut_decode_string+=[string[i:i+step]]
  print("Столбцы: " + str(cut_decode_string))

  indexes=[]
  for item in sorted_variants:  # 6) каждому элементу в комбинациях - свой индекс
    indexes.append(get_indexes(item))
  print("Комбинации: " + str(sorted_variants))
  print("Индексы элементов в комбинациях: " + str(indexes))

  dic_list=[]
  for i in range(len(indexes)):  # 7) соотносим стобцы и индексы
    dic_list.append(dict(zip(cut_decode_string,indexes[i])))
  # print(dic_list)
  # print(len(dic_list))

  sorted_dic_list=[]
  for dic in dic_list:  # 8) сортируем по порядку индексов и получаем список столбцов в нужном порядке (без индексов)
    sorted_dic_list.append([k for k in sorted(dic, key=dic.get)])
  # print(sorted_dic_list)
  
  cut_into_symbols=[]
  for lst in sorted_dic_list:  # 9) разделяем по символам все столбцы
    cut_into_symbols.append(cut_string(lst))
  # print(cut_into_symbols)

  for item in cut_into_symbols:  # 10) составляем таблицу из элементов - столбцов и транспонируем 
    nparr=np.c_[item].T
    print(nparr)
    ans=''.join([''.join(row) for row in nparr])
    print("Расшифровка: " + str(ans))


nums = ["1","2","3","4","5","6","7","8","9"]
string = "БСЕАГНМЗЛАЕООЯНПЛТБНАЕЕСЬЬЕА"
key = "2X41XX7"

answer = []

decode(nums, string, key, answer)