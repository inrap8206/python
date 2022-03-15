# 리스트 생성
colors = list()
colors = []



# slicing
## [시작 인덱스:끝 인덱스+1:스텝]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0:2]  # [0, 1]
a[3:]  # [3, 4, 5, 6, 7, 8, 9]
a[:8:2]  # [0, 2, 4, 6]



# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]

a + b  # [1,2,3,4,5,6]
a * 3  # [1,2,3,1,2,3,1,2,3]



# 요소 확인
fruit = ['banana', 'apple', 'orange']

'apple' in fruit  # True
'cherry' in fuit  # False



# 수정 및 삭제
a = [1,2,3]

a[2] = 8
a  # [1,2,8]

del a[0]
a  # [2,8]



# 패킹 언패킹
t = [1, 2, 3]
a, b, c = t



# append(x)   # 기존 리스트 끝에 x 삽입
colors.append("red")


# remove(x)   # 리스트에서 첫 번째로 나오는 x를 제거
colors.remove("red")


# sort()     # 리스트의 항목을 오름차순으로 정렬
a = [1, 7, 9, 2, 5]
a.sort()     # [1, 2, 5, 7, 9]
a.sort(reverse=True)    # 내림차순


# sorted()   # 정렬된 리스트를 리턴값으로 반환
a1 = a.sorted(a)  # [1, 2, 5, 7, 9]
a2 = a.sort(a)    # None


# reverse()  # 리스트의 항목의 순서를 역순으로 뒤집어 줌
a = [1, 7, 9, 2, 5]
a.reverse()       # [5, 2, 9, 7, 1]


a = [45, 87, 99, 21, 55]
max(a)   # 리스트 내 최대값 요소 99
min(a)   # 리스트 내 최소값 요소 21
sum(a)   # 리스트 내 요소값 합  307
