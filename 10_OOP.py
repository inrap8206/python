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

