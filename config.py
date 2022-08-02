#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
#SQLALCHEMY_DATABASE_URI => 데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_TRACK_MODIFICATIONS => SQLAlchemy의 이벤트 처리하는 옵션
#해당 옵션은 현재 예제에서 불필요로 False로 비활성화

SECRET_KEY="824wjdwkr!"

