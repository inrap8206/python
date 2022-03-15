# while문 : 조건이 True인 동안 A를 반복 수행
number = 1
while number <= 5 :
    print (number)
    number = number + 1


# range(start, stop, step)
range(5, 10)   # [5, 6, 7, 8, 9]
range(1,7,2)   # [1, 3, 5]



# for문 : 순서열을 순회하다가 순서열의 끝에 도달하면 반복을 종료
for 반복변수 in 순서열:
    반복할 문장

    
    
# break : 반복문 순회 도중 break 문을 만나면 내부 블록 벗어남
for i in range(1, 11):
    if i > 5:
        break
    print(i)

    
    
# continue : 반복문 순회 도중 continue 문을 만나면 그 아래의 문장은 해당 반복에 한해서 건너뜀
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

    
    

#단어(문자열)가 주어질 때, 아래와 같이 출력되도록 작성하시오.
#while문을 이용하여 작성(문자열)
word = "Python"

i = 0
while i < len(word):
    print(word[i])
    i += 1

    
#아래와 같이 출력되는 프로그램을 작성하시오.
for i in range(10,0,-1):
    print(i, end=',')
print('Happy new year!!')


#양의 두 정수 a, b를 입력 받아, a부터 b까지의 정수의 합을 구하여 출력하는 프로그램을 작성하시오.
#(for 또는 while을 이용할 것) 단, 조건 a <= b 을 만족하는 값만 고려한다.
nums = input("Enter two integers: ")
a, b = map(int, nums.split())
ab_sum = 0
for i in range(a, b+1):
    ab_sum += i
print("The sum from %d to %d is %d" % (a, b, ab_sum))


#주어진 문자열에 문자a가 몇 개 있는지 구하는 프로그램을 작성하시오.(for문 사용할 것)
word = 'banana'
n = 0
for c in word:
    if c == 'a':
        n += 1
print(n)


#for 문과 range()함수를 이용하여 다음과 같이 출력되도록 작성하시오. (각 줄마다 range()함수 사용)
for i in range(0,10):
    print(i, end=' ')
print()
    
for i in range(0,51,5):
    print(i, end=' ')
print()      # 0 5 10 15 20 25 30 35 40 45 50 

for i in range(10,0,-1):
    print(i, end=' ')
print()      # 10 9 8 7 6 5 4 3 2 1


#for 문을 사용하여 리스트(colors)의 모든 내용을 출력하시오. (단, range()를 이용하지 않는다.)
colors = ["red", "green", "blue"]
for i in colors:
    print(i)
    
    
#리스트 a 전체를 반복해서 방문하되, 짝수만 출력하시오.(for 문 사용)
a = [1,3,4,5,6,7,8,9,10,11,12,13]
for i in a:
    if i % 2 == 0:
        print(i, end=' ')    # 4 6 8 10 12 
        
        
#구구단 출력1
a = int(input("출력하고 싶은 단을 입력하세요:"))
for i in range(1, 10):
    print("%d * %d = %2d" % (a, i, a*i))
    
    
#구구단 출력2
for n in range(2,10):
    print("== %d단 ==" % n)
    for i in range(1, 10):
        print("%d * %d = %2d" % (n, i, n*i))
        
        
#구구단 출력2 (중첩 반복문)
i, k, guguline = 0, 0, ""
for i in range(1, 10):
    guguline = ""
    for k in range(2, 10):
        guguline = guguline + str("%d * %d = %2d  " % (k, i, k*i))
    print(guguline)
    
    
#★ 출력 프로그램
num = input("Input an integer: ")
for i in num: 
    print("★"*int(i))
    
    
#“done“을 입력할 때까지 사용자로부터 숫자를 입력받아 리스트에 저장하고,
#“done“을 입력하면, 리스트의 평균, 최대값과 최소값을 출력하는 프로그램을 작성하시오.
num = input("Enter a number:")
num_ls = []
while num != "done":
    num_ls.append(float(num))
    num = input("Enter a number:")

print()
print(num_ls)
print("Average: %.1f" % (sum(num_ls)/len(num_ls)))
print("Maximum: %.1f" % max(num_ls))
print("Minimum: %.1f" % min(num_ls))
