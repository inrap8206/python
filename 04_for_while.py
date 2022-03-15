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


#양의 정수 a와 b를 받아 a부터 b까지 곱한 값을 반환하는 mult 함수를 작성하시오.
def mult(a,b):
    result = 1
    for i in range(a, b+1):
        result *= i
    return result

print(mult(1,3))
print(mult(2,5))


#1개 이상의 2차원 벡터들을 받아, 벡터들의 합을 구하여 반환하는 함수를 작성하시오 (적어도 1개는 반드시 입력되어야함).
def vector_sum(vector, *vectors):
    vector1 = list(vector)
    for vector_ in vectors:
        vector1[0] += vector_[0]
        vector1[1] += vector_[1]
    return vector1


v1=[0, 1]
v2=[0.5, 0.5]
v3=[1, 0]
v4=[6, 4]
v5=[3.14, 2.72]
m1=vector_sum(v1,v2,v3)
m2=vector_sum(v1,v2,v3,v4)
m3=vector_sum(v3,v5)
print(m1,m2,m3)


#로또 번호 자동 기입 프로그램을 작성하시오
#(5개의 로또 번호 자동 기입 결과 작성. 각 로또 번호 자동 기입 결과는 1~45의 숫자 중 6개를 임의로 선택하여
#정렬한 후 출력되어야 하며, 각 자동 기입에서 중복되는 숫자가 있어서는 안된다.)
import random
nums = list(range(1,46))
print("** 로또 번호 자동 기입을 시작합니다. **")
for i in range(1, 6):
    result = random.sample(nums,5)
    result.sort()
    print("%d번째 자동 기입 ==>" % i, *result)
