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
