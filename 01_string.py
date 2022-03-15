# formatting
print("I eat %d apples." %3)

number = 10
day = "three"
print("I ate %d apples, so I was sick for %s days." % (number, day))

# string function
word = 'Python'
len(word) # 6
word.count('y')  # 1
word.index('n')  # 5
a = ','
a.join('1234') # '1,2,3,4'
s1 = 'python is fun'
s1.split()  # ['python', 'is', 'fun']
s2 = 'one:two:three'
s2.split(":")  # ['one', 'two', 'three']


#화씨온도(℉)를 입력 받아서 섭씨온도(℃)로 바꾸는 프로그램을 작성하시오. 
fd = int(input("화씨온도: "))
cd = (fd-32)*5/9
print("섭씨온도: %.10f" % cd)


#문제2 자동 판매기 프로그램
#사용자로부터 투입한 돈과 물건 값을 입력 받아, 잔돈을 계산하여 출력한다.
# 단, 동전의 개수는 최소화 할 것

money = int(input("투입한 돈: "))
price = int(input("물건값: "))

balance = money - price

coin1 = balance//500
coin2 = balance%500//100
print("거스름돈:", balance)
print("500원짜리: %d개" % coin1)
print("100원짜리: %d개" % coin2)


#원의 반지름을 r을 입력 받아, 원의 둘레와 넓이를 구하는 프로그램을 작성하시오
r = int(input("반지름을 입력하시오:"))
pi = 3.141592
cicle = 2*pi*r 
area = pi*r**2
print("원 둘레: %.2f" % cicle)
print("원 넓이: %.2f" % area)


#2개의 정수를 입력 받아, 사칙연산 및 나머지 연산의 결과를 아래와 같이 출력하는 프로그램을 작성 하시오.
nums = input("Enter two integers:")
num1, num2 = map(int, nums.split())
print(num1, '+', num2, '=', num1+num2)
print(num1, '-', num2, '=', num1-num2)
print(num1, '*', num2, '=', num1*num2)
print(num1, '/', num2, '=', num1/num2)
print(num1, '%', num2, '=', num1%num2)


#두 정수를 입력 받아, 합과 평균을 구하여 출력하는 프로그램을 작성하시오.
nums = input("Enter two integers:")
num1, num2 = map(int, nums.split())
print("The sum of %d and %d is %d" % (num1, num2, num1+num2))
print("The average of %d and %d is %.1f" % (num1, num2, (num1+num2)/2))



date = input("날짜(연/월/일)입력: ")
yyyy, mm, dd = date.split('/')
print("입력한 날짜의 10년 후는 %d년 %d월 %d일" %(int(yyyy)+10, int(mm), int(dd)))
