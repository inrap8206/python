'''bool 자료형
bool은 True와 False 두 가지 값을 나타내는 자료'''

result = 3 > 2
print(result)   # True
type(result)    # <type'bool'>

bool(0)  # False
bool([1,2,3])  # True

#입력 받은 정수가 짝수인지 홀수인지 판별
number = int(input("Enter a number:"))
if number%2 != 0:
    print(number, "is Odd number")
else:
    print(number, "is Even number")
    
    
#프로그래밍 과목의 중간고사와 기말고사 점수를 입력 받아 평균과 학점을 구하는 프로그램을 작성하시오.
m_score = int(input("Enter your midterm score:"))
f_score = int(input("Enter your final score:"))
a_score = (m_score+f_score)/2
grade = 'F'

if a_score >= 90:
    grade = 'A'
elif a_score >= 80:
    grade = 'B'
elif a_score >= 70:
    grade = 'C'
elif a_score >= 60:
    grade = 'D'

print("Average", a_score)
print("Grade", grade)


#학생수준평가 시험에서 영어 점수와 수학 점수가 합해서 110점 이상이면 합격이다.
#단, 각 점수가 40점 미만이면 불합격이다. 영어(eng), 수학(math)점수를 입력 받아 합 격여부를 출력하는 프로그램을 작성하시오
eng = int(input("영어 점수 입력:"))
math = int(input("수학 점수 입력:"))
total = eng+math

if total < 110 : print('불합격: 총합 점수 부족')
elif eng < 40: print('불합격: 영어 점수 부족')
elif math < 40: print('불합격: 수학 점수 부족')
else: print('합격')
  
  
#세 개의 정수를 입력 받아, 가장 큰 수만 출력하는 프로그램을 작성하시오. (max 함수 이용하지 않고 구할 것)
num1, num2, num3 = map(int, input("세 개의 수를 입력하시오:").split())
max_num = num1
for i in [num2, num3]:
    if max_num < i:
        max_num = i
print("가장 큰 수는 %d입니다." % max_num)
