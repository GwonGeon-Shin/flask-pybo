#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 이하 form 입력 내용 기재 되어야 하지만 본 프로젝트에서는 아직
# 입력 부분에 대한 기능을 구현하지는 않음

class UserCreateForm(FlaskForm): #회원가입 폼
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')
    ])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    
class UserLoginForm(FlaskForm):
    username = StringField('사용자 E메일', validators=[DataRequired(), Email()])
    # ㄴ> 로그인시 id값 e메일로 받아라
    password = PasswordField('비밀번호', validators=[DataRequired()])

class UserPassNew(FlaskForm): # 비밀번호 신규 생성위한 class
    #username = StringField('사용자 E메일', validators=[DataRequired(), Email()])
    # ㄴ> 로그인시 id값 e메일로 받아라
    password1 = PasswordField('신규 비밀번호', validators=[
        DataRequired(), EqualTo('password2', '재확인 비밀번호가 일치하지 않습니다.')
        ])
    password2 = PasswordField('입력 재확인', validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('입금일자', validators=[DataRequired('입금일은 필수입력 항목입니다.')])