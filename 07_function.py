'''
함수 사용이유: 코드 재사용, 절차적 분해
'''

# 함수 정의
def add(a, b):
  result = a + b
  return result


# 함수 호출
add_result = add(100, 200)
print(add_result)


# 가변 매개변수
def 함수이름 (*매개변수):
    수행할 문장
    
def count_even(*n):
  cnt= 0
  for v in n:
    if v % 2 == 0:
      cnt += 1
  return cnt
    

# 매개변수 기본값 설정
def printName (first, second='Kim'): #second 변수 기본값 'kim'
    print ('My name is', first, second + '.')
    
printName('Gildong', 'Hong')
printName('Gildong')


# 앞 매개변수가 디폴트 값을 가지면, 뒤에 오는 매개변수는 반드시 디폴트 값을 가져야 함
def printName(first, second='Kim'): # 정상
def printName(first='Kim', second): # 에러 발생
def printName(first, second, third='Kim'): # 정상
def printName(first, second='Kim', third='M'): # 정상


# 함수 호출 시 , 해당 매개변수 이름을 명시적으로 지정해서 전달
def calc(x, y=0, z=0):
  return x+y z

result = calc (y=20, x=10, z=30) # 매개변수 순서 상관 없음
print(result)

calc(y=20, x=10) # 정상
calc(10, y=30, z=20) # 정상
calc(10, 30, y=20) # 에러 발생
 
  
# 양의 정수 a와 b를 받아 a부터 b까지 곱한 값을 반환하는 mult 함수를 작성하시오.
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


'''
[지역변수]
- 함수 안에서 만들어져 함수 안에서만 사용하는 변수
- 함수 내에서 정의된 변수는 함수 내에서만 사용해야 한다
- 함수 외에서 정의된 변수를 사용할 경우 주의가 필요하다
'''
def add_value(a , b):
  add_res = a + b
  return add_res

x = 10
y = 20
res = add_value(x, y)
print(add_res) # 에러 발생



'''
[전역변수]
- 함수 밖에서 만들어져 아무데서나 사용 수 있는 변수
- 함수 내에서 수정하기 위해선 , “global” 문구로 전역변수임을 명시
'''
def addX(_x):
  x = x + _x # 에러 발생

def addX(_x):
  global x   # 전역변수임을 명시
  x = x + _x 
  
x = 10
y = 20

addX(y)
print(x)


'''
[재귀함수]
- 자기 자신을 호출하는 함수 (Recursive Function)
- 함수 내에 자기 자신을 호출하지 않는 종료 조건이 없다면, 무한히 반복
'''

def counting(n):
  print(n)
  counting(n+1)

counting(1)


def my_sum(n):
  if n == 1:  # 종료 조건
    return 1
  return n + my_sum(n-1)

my_sum(10)
