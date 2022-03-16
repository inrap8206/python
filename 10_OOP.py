'''
Object-Oriented Programming : 객체지향 프로그래밍
객체란 모종의 변수와 메서드를 담는 추상적 개념
python은 모든것이 객체임  ex) list, string, int, function

Class : 데이터와 함수를 묶어 객체로 만들어 주는 개념. 객체의 기반이 되는 틀을 정의함.
'''

# Class의 구성요소 : 변수와 메서드
class Dog:
  name = 'coco'     # 변수
  def bark(self):   # 메서드. 객체 자신을 지정하는 첫번째 인자 self가 항상 존재해야 함
    return 'wal wal'

dog1 = Dog()        # 인스턴스 생성
dog1.name           # 'coco'
dog1.bark()         # 'wal wal'
  

'''
__init__ : 생성자. 인스턴스 생성시 자동으로 호출되는 특수 메서드*
인스턴스가 갖게 될 여러 속성을 정해주는 역할
*특수 메서드 :  "__메서드이름__" 형태이며, 내장함수와 동일하게 미리 동작이 정의되어 있음
'''
class Sample:
  def __init__(self):
    # statement
    return None  # 무조건 retunr은 None이어야 함 또는 생략 가능

class Building:
  def __init__(self, name='공학관', h=3, elev=True):
    self.name = name
    self.h = h
    self.elev = elev
    
  def get_info(self):
    print("건물이름=", self.name)
    print("건물층수=", self.h)
    print("엘리베이터 유무=", self.elev)

    
'''
Inheritance(상속) : 기존 클래스의 속성을 물려 받아 새로운 클래스를 만드는 것
 - 새 클래스는 기존 클래스의 모든 변수 및 메서드를 가짐
 - 주로 기존 클래스를 확장하는 용도로 사용
 - 다중 클래스도 상속 가능 ","로 구분   ex)  class sample_sub(sample_super1, sample_super2):
'''

class A:
  a = 1
  def print_a():
      print("A class")
      
class B:
  b = 1
  def print_b():
      print("B class")
      
class C(A):    # A 클래스 상속
  c = 1
  def print_c():
      print("C class")
      
class D(C,B):
  d = 1
  def print_d():
      print("D class")

      
'''
Method Overriding : 기존 클래스 메서드를 상속 클래스에서 재 정의 하는 것
 - 재정의하지 않은 메서드는 기존 클래스의 것을 그대로 사용
 - 오버라이딩한 경우 기존 클래스의 메서드를 사용하고자 하는 경우 'super()' 사용
'''

class A():
  def __init__(self):
      print("this is [A] class and [__init__] fuction")
      self.var1 = 0
      self.var2 = 0
      
class B(A):
  def __init__(self):
      super().__init__()
      print("this is [B] class and [__init__] function")
      self.var3 = 0
      self.var4 = 0
      
a = A()
b = B()


'''
Operator Overloading : 내장된 특수 메소드를 호출하여 객체에 맞는 방법으로 사용가능하게 함
  - 해당 메서드를 override 하는 것으로 기능을 변경
  - ex) a + b 는 자동으로 a.__add__(b)를 호출함
'''
class BankAccount:
    def __init__(self, balance=0, name='none'):
        self.balance = balance
        self.name = name
        
    def deposit(self, amount):
        self.balance += amount
        
    def __add__(self, amount):
        self.deposit(amount)
        
    def __iadd__(self, amount):
        self.deposit(amount)
        
a = BankAcount(1000, "kim")
print(a.balance)    # 1000

a + 1000    # a.__add__(1000)와 같음
print(a.balance)    # 2000



'''
Iterator : iterable* 가능한 객체로 만들어 주는것
*iterable : 리스트와 같이 한개씩 꺼내어 쓸수 있는 형태로 for문에서 in 다음에 입력하여 사용이 가능
  - iterable 가능한 객체는 '__iter__()' 메서드를 가지도 있음
'''
class PowTwo:
    """Class to impliment an iterator of powers of two"""
    
    def __init__(self, start=0)
        self.start = start
      
    def __iter__(self):
        return self
      
    def __next__(self):
        result = 2 ** self.start
        self.start += 1
        return result
      
a = PowTwo(3)
myiter = iter(a)
print(next(myiter))   # 8
print(next(myiter))   # 16
print(next(myiter))   # 32


'''
Generator
“yield”를 사용하여 데이터를 하나씩 반환하는 함수
  - 이터레이터와 같은 동작수행, 하지만 보다 간단
  - 함수객체 생성시 __iter__() 와 __next()__ 메서드 자동생성
  - 일반적인 함수처럼 작성되지만 값을 반환하고 싶을 때마다 ”yield”문을 사용
  - 마지막 반환 결과를 기억, 재호출시 그 위치부터 다시 시작
  - 데이터가 대량일 경우 일부씩 처리시 유용
  - On demand 계산을 하나씩 처리하고 싶은 경우
'''
def gen():
    for i in range(5):
        yield i 
g = gen()
print(next(g))    #0
print(next(g))    #1
print(next(g))    #2


def square_numbers(nums):
    for x in nums:
        yield x * x
        
numbers = range(1000000000000)
g = square_numbers(numbers)

print(next(g))    # 0
print(next(g))    # 1
print(next(g))    # 4
print(next(g))    # 9



      
# 은행 계좌 클래스 만들기
class BankAccount:
  def __init__(self, balance=0, name='none'):
    self.balance = balance
    self.name = name
    
  def withdraw(self, amount):
    if self.balance >= amount:
       self. balance -= amount
    else:
      print('잔액부족')
      
  def deposit(self, amount):
    self.balance += amount
    
  def get_info(self):
    print('이름: ', self.name)
    print('잔고: ', self.balance)
    
    
# 최소 잔액을 유지하는 계좌 클래스 만들기 (상속 이용)
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, name='none', min_bal=0):
        self.balance = balance
        self.name = name
        self.min_bal = min_bal
    
    def withdraw(self, amount):
      if self.balance - amount < self.min_bal:
         print('최소 잔액을 유지해야합니다.')
      else:
         super().withdraw(amount)        # 상속받은 클래스 내 함수 그대로 사용
          
a = MinimumBalanceAccount(1000, "kim", 500)
a.withdraw(100)



# Operator Overriding 예제
class Set:
    def __init__(self, L):
        self.L=[]
        for i in range(len(L)):
            flag=True
            for j in range(i):
                if L[i] == L[j]:
                    flag=False
            if flag:
                self.L.append(L[i])
        
    def add(self, elem):
        if elem not in self.L:
            self.L.append(elem)
        else:
            pass
    
    def discard(self, elem):
        if elem in self.L:
            self.L.remove(elem)
            
    def clear(self):
        self.L = []
        
    def __len__(self):
        return len(self.L)
    
    def __str__(self):
        return "{" + str(self.L)[1:-1] + "}"
    
    def __contains__(self, elem):
        result = True
        if elem in self.L:
            pass
        else:
            result = False
        return result
        
    def __le__(self, other): # other=Set()
        result = True
        for x in self.L:
            if x in other.L:
                pass
            else:
                result = False
        return result
        
    
    def __ge__(self, other): # other=Set()
        result = True
        for x in other.L:
            if x in self.L:
                pass
            else:
                result = False
        return result     
    
    def __or__(self, other): # other=Set()
        result = self.L[:]
        for i in other.L:
            if i not in result:
                result.append(i)
        r = Set(result)
        return r
    
    def __and__(self, other): # other=Set()
        result = []
        for i in other.L:
            if i in self.L:
                result.append(i)        
        r = Set(result)
        return r
    
    def __sub__(self, other): # other=Set()
        result = []
        for i in self.L:
            if i not in other.L:
                result.append(i)        
        r = Set(result)
        return r 
    
    def __ior__(self, other): # other=Set()
        for i in other.L:
            if i not in self.L:
                self.L.append(i)
        return self
    
    def __iand__(self, other): # other=Set()
        result = []
        for i in other.L:
            if i in self.L:
                result.append(i)     
        self.L = result[:]
        return self
    
    def __isub__(self, other): # other=Set()
        result = []
        for i in self.L:
            if i not in other.L:
                result.append(i)  
        self.L = result[:]
        return self
