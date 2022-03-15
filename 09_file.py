f = open("input.txt", "r")  # 읽기 모드
f = open("input.txt", "w")  # 쓰기 모드
f = open("input.txt", "a")  # 추가 모드

f.close()  # 파일 닫기



f = open("new.txt", "w")
for i in range(1, 6):
  data = "%d line\n" % i
  f.write(data)
f.close()
  
  
f= open("new.txt", "r")
line = f.readline()    # 한줄 읽어옴
print (line, end='')   # 1 line
line = f.readline()    # 다음 한줄 읽어옴
print (line, end='')   # 2 line
f.close()


f= open("new.txt", "r")
lines = f.readlines()   # 모든 라인을 한꺼번에 읽어서 각각의 줄을 요소로 갖는 리스트를 반환
print (lines)           # ['1 line\n', '2 line\n', '3 line\n', '4 line\n']
f.close()


f = open("new.txt", "r")
data = f.read()         # 파일을 전부 읽은 문자열을 반환
print (data, end='')
f.close()


f = open("new.txt", "r")
for line in f:              # for 문 사용
  print (line, end='')
f.close()


f = open("new.txt", "a")   # 파일에 내용 추가
for i in range(6, 11):
  data = "%d line\n" % i
  f.write(data)
f.close()


with open( "output.txt", "w" ) as f :    # 파일을 열고 자동으로 닫기
  f.write("Python is fun!")              # with 블록을 벗어나는 순간 파일을 자동으로 닫음
  
  
f.tell()    # 현재 파일 포인터의 위치 반환
f.seek()    # 지정하는 곳으로 포인터의 위치를 변경
f = open("test.txt", "r")
f.tell()        # 0
f.readline()    # 'first line\n'
f.tell()        # 11


'''
[sys모듈]
도스나 리눅스 쉘에서 파이썬 명령어를 실행하면서 입력인수를 넣어줄 수 있음.
ex) $ python sys1.py aaa bbb ccc
 - argv[0] = sys1.py
 - argv[1] = aaa
 - argv[2] = bbb
 - argv[3] = ccc
'''
#sys1.py
import sys
args= sys.argv[1:]
for i in args:
  print (i)

  
#파일에 있는 각각의 단어 수 구하기
f = open("test.txt", "r")
data = f.read()
f.close()
l = data.split()
for word in set(l):
    print(word, l.count(word))
f.close()


#파일명을 입력 받아받아, 해당 파일을 한 줄씩 읽어 파일의 내용을 모두 대문자로 출력하는 프로그램을 작성하 시오시오.
#단, 파일이 없는 경우 “파일이 존재하지 않는다않는다" 정도의 메시지를 출력할 것!
file_name = input("Enter a file name:")

import os
if os.path.exists(file_name):
    f = open("test.txt", "r")
    for line in f:
        print(line.upper(), end='')
else: 
    print("파일이 존재하지 않는다.")
f.close()


#아래의 score.txt를 읽어서 학생들의 성적을 처리하여 그 결과를 report.txt로 출력하는 프로그램을 작성하시오.
fr = open("score.txt", "r")
fw = open("report.txt", "w")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for line in fr:
    a = line.split()
    total = int(a[1])*0.4 + int(a[2])*0.6
    grade = get_grade(avg)
    print_line = "%s %s %s   %.1f(%s)\n" % (a[0], a[1], a[2], total, grade) 
    fw.write(print_line)    
fr.close()
fw.close()
