import numpy as np

# Iterable 객체 이용 배열 생성
a = np.array([2, 3, 4])


# 데이터 타입 지정
c = np.array([[1,2], [3,4]], dtype=complex)


# 사전 정의된 shape의 배열 생성
np.zeros((3,4))
np.ones((2,3,4), dtype=np.int16)
np.empty((2,3))
np.arange(10, 30, 5)    # range와 같은 기능
np.arrange(0, 2, 0.3)   
np.linespace(0, 2, 7)   # start, end, 개수, np.arrange(0,2,0.3)실행과 비슷한 결과
np. arrange(24).reashape(2, 3, 4)
[[[ 0 1 2 3]
  [ 4 5 6 7]
  [8 9 10 11]]
 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]


# 인덱싱  [start: stop: step]
## 리스트 슬라이싱과 같으나, 슬라이싱으로 변수 저장시
## shallow copy로 저장됨. deepcopy 필요시 numpy.copy()호출
np.arrange(35).reshape(5, 7)
y[1:5:2, ::3]
array([[7, 10, 13], [21, 24, 27]])


# 배열 shape 수정
a.resize(2,6)
a.resize(3,-1)    # -1 지정시 자동 계산
np.vstack((a,b))
[[1 2]
 [3 4]
 [5 6]
 [7 8]]

np.hstack((a,b))
[[1 2 3 4]
 [5 6 7 8]]


# 테두리가 1, 속은 0(또는 반대)인 5 x 5 배열을 만드시오
import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("New array:")
x[1:-1, 1:-1] = 0
print(x)




