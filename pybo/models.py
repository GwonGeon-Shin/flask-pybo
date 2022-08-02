#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from enum import unique
from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 기본키 생성, 고유값
    our_ref = db.Column(db.Text(), unique=True, nullable=True) # 엑셀시트 근거 (OurRef 자료) #unique로 중복관리
    pay_date = db.Column(db.Text(), nullable=True) # 요청에 근거(신규생성, 입금일자)
    req_name = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (의뢰인 자료)
    cus_name = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (출원인 자료)
    date = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (출원일 자료)
    number = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (출원번호 자료)
    q_date = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (우선심사청구일 자료)
    q_d_date = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (우선심사결정일 자료)
    d_d_date = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (등록일 자료)
    d_d_num = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (등록번호 자료)
    p_name = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (국문명칭 자료)
    charge_01 = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (담당자01 자료)
    charge_02 = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (담당자02 자료)
    p_charge = db.Column(db.Text(), nullable=True) # 엑셀시트 근거 (변리사명 자료)
    create_date = db.Column(db.DateTime(), nullable=True) # 자료 작성일시 기록


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True) # 회원관리번호_고유키
    email = db.Column(db.String(120), unique=True, nullable=False) # e메일을 로그인 id값으로 사용할 예정
    username = db.Column(db.String(150), unique=True, nullable=False) # 사용자 이름, #unique=True 는 같은값을 저장할수 없다는 의미
    password = db.Column(db.String(200), nullable=False)


    

