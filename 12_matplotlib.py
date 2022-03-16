'''
Matplotlib : PYTHON 용 도표 작성 라이브러리
  - 라인 플롯 (line plot)
  - 스캐터 플롯 (scatter plot)
  - 컨투어 플롯 (contour plot)
  - 서피스 플롯 (surface plot)
  - 바 차트 (bar chart)
  - 히스토그램 (histogram)
  - 박스 플롯 (box plot)
  
pyplot 서브모듈을 사용하여 도표를 그림
  - MATLAB과 유사한 인터페이스 제공
  - 하나의 함수 호출로 다양한 종류의 도표 즉시 작성 가능
  
Jupyter Notebook에서 사용 시 아래 명령 사용
  - %matplotlib inline
  - 한 번 호출해두면 Notebook 화면 내에서 이미지 직접 표시
'''

# 선그리기
import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 100)  # 0~10 구간을 100개로 쪼갬
b = np.exp(-a)
plt.plot(a, b)    # x축:a, y축:b
plt.show()        # 도표 출력


# 여러개 선그리기
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()



# 히스토그램
from numpy.random import normal
x = normal(size=200)
plt.hist(x, bins=30)    # x축을 30개의 구간으로 분절
plt.show()


# 산점도 그리기
from numpy.random import rand
a = rand(100)
b = rand(100)
plt.scatter(a, b)
plt.show()

# 도표의 구성요소
https://matplotlib.org/stable/gallery/showcase/anatomy.html
  

# 도표 설정 함수
plt.title(label)    # 제목 설정
plt.legend()        # 범례 표시 설정
plt.xlabel()        # x축 이름 설정
plt.ylabel()        # y축 이름 설정


# 도표 여러개 작성1
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100000)
y = .4 * x + np.random.randn(100000) + 5

fig, axs = plt.subplots(1, 2, sharey=True)

print(type(axs))
axs[0].hist(x, bins=20)
axs[1].hist(y, bins=20)

fig.suptitle("Histograms")
plt.show()


# 도표 여러개 작성2
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 3.0, 200)
a = x
b = x**2
c = np.exp(x)
d = np.log(x)

fig, axs = plt.subplots(2, 2, sharey=True)

print(type(axs))

axs[0,0].plot(x, a, '-g', label='linear')
axs[0,1].plot(x, b, '--r', label='quadratic')
axs[1,0].plot(x, c, ':b', label='exponential')
axs[1,1].plot(x, d, '--y', label='logarithmic')

fig.text(0.5, 0.04, 'common X', ha='center')
fig.text(0.04, 0.5, 'common y', va='center', rotation='vertical')
fig.suptitle("Simple Plot")
plt.show()
