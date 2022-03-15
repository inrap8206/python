# 모듈 : 많이 사용하는 함수들의 덩어리
# 모듈로 사용할 파일과 호출하는 파일은 모두 같은 폴더에 저장 

# 모듈 호출
import module_name            # 기본적인 모듈 불러오기
import module_name as mn      # 모듈에 다른 이름을 붙이기
from module_name import func  # 특정 함수만 불러오기

# ramdom
import random

random.choice('abcde')    # 리스트에서 랜덤하게 1개 선책
random.randint(a, b)      # a~b 정수 값 중 하나
random.randrange(a, b+1)  # a~b 정수 값 중 하나
random.shuffle([1,2,3,4]) # 리스트 요소 순서 섞기
random.sample([1,2,3,4], 2)  # 리스트 중 2개 뽑기


#로또 번호 자동 기입 프로그램을 작성하시오
#(5개의 로또 번호 자동 기입 결과 작성. 각 로또 번호 자동 기입 결과는 1~45의 숫자 중 6개를 임의로 선택하여
#정렬한 후 출력되어야 하며, 각 자동 기입에서 중복되는 숫자가 있어서는 안된다.)

import random
nums = list(range(1,46))
print("** 로또 번호 자동 기입을 시작합니다. **")
for i in range(1, 6):
    result = random.sample(nums,5)
    result.sort()
    print("%d번째 자동 기입 ==>" % i, *result)
