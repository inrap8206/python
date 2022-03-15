#!/usr/bin/env python
# coding: utf-8

# In[5]:


# slicing
## [시작 인덱스:끝 인덱스+1:스텝]

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0:2]  # [0, 1]
a[3:]  # [3, 4, 5, 6, 7, 8, 9]
a[:8:2]  # [0, 2, 4, 6]


# In[ ]:


# 리스트 연산

a = [1, 2, 3]
b = [4, 5, 6]

a + b  # [1,2,3,4,5,6]
a * 3  # [1,2,3,1,2,3,1,2,3]


# In[ ]:


# 요소 확인

fruit = ['banana', 'apple', 'orange']

'apple' in fruit  # True
'cherry' in fuit  # False


# In[ ]:


# 수정 및 삭제

a = [1,2,3]

a[2] = 8
a  # [1,2,8]

del a[0]
a  # [2,8]


# In[ ]:


# 패킹 언패킹

t = [1, 2, 3]

a, b, c = t

