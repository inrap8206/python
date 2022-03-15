'''
딕셔너리는 중괄호{}로 묶여 있으며, key와 value의 쌍으로 이루어짐
d = {key1:value1, key2:value2}
- key는 중복 될 수 없음
- 항목들 사이에 순서가 없음
'''

d = {}
d['kim'] = 1 # 새 항목 추가
d['park'] = 2 # 새 항목 추가
d   # {'park': 2, 'kim': 1}

d['kim'] = 3  # 기존 값 변경
d  # {'park': 2, 'kim': 3}


d.keys() # 키만 추출 dict_keys(['kim', 'park', 'youn'])
d.values() # 값만 추출 dict_values([3, 2, 1])

# 키와 값의 항목을 튜플 형태로
d.items()  # dict_items([('kim', 3), ('park', 2), ('youn', 1)])

# 딕셔너리에 키가 있는 경우
'kim' in d   # True

# 딕셔너리에 키가 없는 경우
'lee' in d  # False


d   # {'youn': 1, 'park': 2, 'kim': 3}
del d['kim']   # {'youn': 1, 'park': 2}
d.clear()      # {}



#for 문을 사용하여 딕셔너리 타입의 d의 모든 value를 출력해 보시오.
d= {'yoon': 1, 'park': 2, 'kim': 10}
for i in d:
    print(d[i], end=' ')
    
    
#아래와 같은 딕셔너리가 있다.
dic1 = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
key_ls = list(dic1.keys())
key_ls.sort()
for i in key_ls:
    print("%s %d" % (i, dic1[i]))    
    
    
#어떤 문장을 입력 받으면 해당 문장에서 각 문자가 몇 개씩 나오는지 저장하는 딕셔너리를 만든 후, 아래와 같이 출력하시오.
a = input("Enter a sentence:")
d = {}
for i in a:
    d[i] = a.count(i)
print(d)
